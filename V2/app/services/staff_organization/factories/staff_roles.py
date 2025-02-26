from typing import List
from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from V2.app.services.staff_organization.validators import StaffOrganizationValidators
from V2.app.database.models.staff_organization import StaffRoles
from V2.app.database.db_repositories.sqlalchemy_repos.core_repo import SQLAlchemyRepository
from V2.app.database.models.data_enums import ArchiveReason


SYSTEM_USER_ID = UUID('00000000-0000-0000-0000-000000000000')

class StaffRolesFactory:
    """Factory class for managing staff role operations."""

    def __init__(self, session: Session):
        """Initialize factory with database session.
        Args:
            session: SQLAlchemy database session
        """
        self.repository = SQLAlchemyRepository(StaffRoles, session)
        self.validator = StaffOrganizationValidators()

    def create_role(self, new_role) -> StaffRoles:
        """Create a new staff role.
        Args:
            new_role: Role data containing name and description
        Returns:
            StaffRoles: Created role record
        """
        role = StaffRoles(
            id=uuid4(),
            created_by=SYSTEM_USER_ID,
            last_modified_by=SYSTEM_USER_ID,
            name=self.validator.validate_name(new_role.name),
            description=self.validator.validate_name(new_role.description)
        )
        return self.repository.create(role)

    def get_all_roles(self) -> List[StaffRoles]:
        """Get all active staff roles.
        Returns:
            List[StaffRoles]: List of active role records
        """
        return self.repository.get_all()


    def get_role(self, role_id: UUID) -> StaffRoles:
        """Get a specific staff role by ID.
        Args:
            role_id: ID of role to retrieve
        Returns:
            StaffRoles: Retrieved role record
        """
        return self.repository.get_by_id(role_id)


    def update_role(self, role_id: UUID, data: dict) -> StaffRoles:
        """Update a staff role's information.
        Args:
            role_id: ID of role to update
            data: Dictionary containing fields to update
        Returns:
            StaffRoles: Updated role record
        """

        existing = self.get_role(role_id)
        if 'name' in data:
            existing.name = self.validator.validate_name(data['name'])
        if 'description' in data:
            existing.description = self.validator.validate_name(data['description'])
        existing.last_modified_by = SYSTEM_USER_ID

        return self.repository.update(role_id, existing)


    def archive_role(self, role_id: UUID, reason: ArchiveReason) -> StaffRoles:
        """Archive a role.
        Args:
            role_id: ID of role to archive
            reason: Reason for archiving
        Returns:
            StaffRoles: Archived role record
        """
        return self.repository.archive(role_id, SYSTEM_USER_ID, reason)


    def delete_role(self, role_id: UUID) -> None:
        """Permanently delete a staff role.
        Args:
            role_id: ID of role to delete
        """
        self.repository.delete(role_id)



