from uuid import uuid4
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, ForeignKey, Enum, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from ..database.models.common_imports import Base
from ..database.models.mixins import AuditMixins, SoftDeleteMixins, TimeStampMixins
from ..database.models.data_enums import UserType, AccessLevel

class Users(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """Boilerplate for all users"""
    __tablename__ = 'users'

    profile_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_type: Mapped[UserType] = mapped_column(Enum(UserType))
    password_hash: Mapped[str] = mapped_column(String(300))
    access_level: Mapped[AccessLevel] = mapped_column(Enum(AccessLevel), default=AccessLevel.USER)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    last_login: Mapped[datetime] = mapped_column(DateTime, nullable=True)



    #Relationships
    staff = relationship('Staff', back_populates='user', foreign_keys="[Staff.profile_id]",
                         primaryjoin="Users.profile_id == Staff.profile_id",uselist=False)

    student =  relationship('Students', back_populates='user', foreign_keys="[Students.profile_id]", uselist=False)

    parent = relationship('Parents', back_populates='user', foreign_keys="[Parents.profile_id]", uselist=False)

    access_changes = relationship('AccessLevelChanges', back_populates='user')

    def __repr__(self) -> str:
        return f"User(profile_id={self.profile_id}, type={self.user_type}, access={self.access_level})"


class AccessLevelChanges(Base, TimeStampMixins, SoftDeleteMixins):
    """Tracks changes to user access levels for audit purposes"""
    __tablename__ = 'access_level_changes'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    profile_id: Mapped[UUID] = mapped_column(ForeignKey('users.profile_id', ondelete='CASCADE'))
    previous_level: Mapped[AccessLevel] = mapped_column(Enum(AccessLevel))
    new_level: Mapped[AccessLevel] = mapped_column(Enum(AccessLevel))
    reason: Mapped[str] = mapped_column(String(500))

    #Audit
    changed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, default=func.now())
    changed_by: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SET NULL'))

    #Relationships
    user = relationship('Users', back_populates='access_changes')

    def __repr__(self) -> str:
        return f"AccessChange(user={self.profile_id}, {self.previous_level}->{self.new_level})"