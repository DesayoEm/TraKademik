from uuid import UUID
from typing import Optional, List, Type
from sqlalchemy import or_, desc, asc
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from sqlalchemy.orm import Session, Query
from V2.app.services.errors.database_errors import (
    UniqueViolationError, EntityNotFoundError, TransactionError, RelationshipError)
from V2.app.services.errors.database_errors import DatabaseError as TKDatabaseError
from V2.app.database.db_repositories.core_repo import Repository, T


class BaseRepository(Repository[T]):
    def __init__(self, model: Type[T], session: Session):
        super().__init__()
        self.model = model
        self.session = session


    def base_query(self) -> Query:
        return self.session.query(self.model).filter(
            self.model.is_archived == False
        )

class SQLAlchemyRepository(BaseRepository[T]):
    """Core CRUD operations"""

    def create(self, entity: T) -> T:
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.refresh(entity)
            return entity
        except IntegrityError as e:
            self.session.rollback()
            if 'unique constraint' in str(e).lower():
                raise UniqueViolationError(
                    field_name=self._extract_constraint_field(str(e))
                )
            elif 'foreign key constraint' in str(e).lower():
                raise RelationshipError(operation = "create", detail=str(e))
        except OperationalError as e:
            self.session.rollback()
            raise ConnectionError(details=str(e))
        except SQLAlchemyError as e:
            self.session.rollback()
            raise TKDatabaseError(error=str(e))


    def get_by_id(self, id: UUID) -> Optional[T]:
        try:
            entity = self.base_query().filter(
                self.model.id == id).first()
            if not entity:
                raise EntityNotFoundError(
                    entity_type=self.model.__name__,
                    identifier=str(id))
            return entity
        except SQLAlchemyError as e:
            raise TKDatabaseError(error=str(e))


    def apply_filters(self, query: Query, fields: List,  filters)-> Query:
        """Apply model-specific filters"""
        if query is None:
            query = self.base_query()

        for field, value in filters.model_dump(exclude_unset=True).items():
            if field in ['limit', 'offset', 'order_by', 'order_dir']:
                continue
            if value is not None and hasattr(self.model, field):
                if isinstance(value, str) and field in fields:
                    query = query.filter(getattr(self.model, field).ilike(f"%{value}%"))
                else:
                    query = query.filter(getattr(self.model, field) == value)

        return query


    def get_all(self, filters, fields) -> List[T]:
        """Get filtered and paginated results"""
        try:
            query = self.base_query()

            for field, value in filters.model_dump(exclude_unset=True).items():
                if field not in ['limit', 'offset', 'order_by', 'order_dir'] and value is not None:
                    query = self.apply_filters(query, fields,filters)
            if hasattr(self.model, filters.order_by):
                order_func = desc if filters.order_dir == 'desc' else asc
                query = query.order_by(order_func(getattr(self.model, filters.order_by)))

            result = query.offset(filters.offset).limit(filters.limit).all()

            if not result:
                raise EntityNotFoundError(entity_type=self.model.__name__)
            return result

        except SQLAlchemyError as e:
            raise TKDatabaseError(error=str(e))



    def update(self, id, updated_entity: T) -> T:
        try:
            existing = self.base_query().filter(self.model.id == id).first()
            if not existing:
                raise EntityNotFoundError(
                    entity_type=self.model.__name__,
                    identifier=str(id)
                )
            self.session.merge(updated_entity)
            self.session.commit()
            self.session.refresh(existing)
            return existing

        except IntegrityError as e:
            self.session.rollback()
            raise UniqueViolationError(
                field_name=self._extract_constraint_field(str(e)))
        except SQLAlchemyError as e:
            self.session.rollback()
            raise TKDatabaseError(error=str(e))


    def archive(self, id, archived_by_id, reason) -> T:
        try:
            entity = self.base_query().filter(
                self.model.id == id
            ).first()
            if not entity:
                raise EntityNotFoundError(
                    entity_type=self.model.__name__,
                    identifier=str(id)
                )

            entity.archive(archived_by_id, reason)
            self.session.commit()
            self.session.refresh(entity)
            return entity
        except SQLAlchemyError as e:
            self.session.rollback()
            raise TKDatabaseError(error=str(e))


    def delete(self, id: UUID) -> None:
        try:
            entity = self.base_query().filter(
                self.model.id == id).first()
            if not entity:
                raise EntityNotFoundError(
                    entity_type=self.model.__name__,
                    identifier=str(id)
                )

            self.session.delete(entity)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise TKDatabaseError(error=str(e))