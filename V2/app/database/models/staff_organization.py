from .common_imports import *
from .mixins import AuditMixins, ArchiveMixins, TimeStampMixins


class StaffDepartments(Base, AuditMixins, TimeStampMixins, ArchiveMixins):
    """
    Represents a staff department.
    Inherits from Base, AuditMixins, TimeStampMixins, and ArchiveMixins.
    """
    __tablename__ = 'staff_departments'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(500))
    manager_id: Mapped[UUID] = mapped_column(ForeignKey('staff.id',
            ondelete='SET NULL', name='fk_staff_departments_staff_manager_id'),nullable=True
        )
    # Relationships
    manager: Mapped['Staff'] = relationship(foreign_keys='[StaffDepartments.manager_id]')

    __table_args__ = (
        Index('idx_department_manager', 'manager_id'),
        Index('idx_staff_department_name', 'name'),
    )


class StaffRoles(Base, AuditMixins, TimeStampMixins, ArchiveMixins):
    """
    Represents a role assigned to a staff member, including the role name and description.
    Inherits from Base, AuditMixins, TimeStampMixins, and ArchiveMixins.
    """
    __tablename__ = 'staff_roles'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(500))

    __table_args__ = (
        Index('idx_role_title', 'title'),
        Index('idx_role_description', 'description'),
    )


class EducatorQualifications(Base, AuditMixins, TimeStampMixins, ArchiveMixins):
    """
    Represents an educator's academic qualifications.
    Inherits from Base, AuditMixins, TimeStampMixins, and ArchiveMixins.
    """
    __tablename__ = 'educator_qualifications'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    educator_id: Mapped[UUID] = mapped_column(ForeignKey('educators.id',
            ondelete='CASCADE', name='fk_educator_qualifications_educators_educator_id')
        )
    title: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)

    # Relationships
    educator: Mapped['Educator'] = relationship(
        'Educator', back_populates='qualifications',
        foreign_keys="[EducatorQualifications.educator_id]"
    )

    __table_args__ = (
        Index('idx_educator', 'educator_id'),
        Index('idx_qualification_title', 'title'),
    )
