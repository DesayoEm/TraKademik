from .common_imports import *
from .mixins import AuditMixins, ArchiveMixins, TimeStampMixins
from .data_enums import (
    DepartmentName, DepartmentCode,
    ClassLevel, ClassCode, StaffDepartmentName)


class Classes(Base, AuditMixins, TimeStampMixins, ArchiveMixins):
    """
    Represents a class within an educational institution, including its level, code, and mentor.
    Links to students and educator mentor relationships.
    Inherits from Base, AuditMixins, TimeStampMixins, and ArchiveMixins.
    """
    __tablename__ = 'classes'

    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    level: Mapped[ClassLevel] = mapped_column(Enum(ClassLevel, name = 'classlevel'))
    code: Mapped[ClassCode] = mapped_column(Enum(ClassCode, name = 'classcode'))
    mentor_id: Mapped[UUID] = mapped_column(ForeignKey('educator.id', ondelete='RESTRICT'))
    student_rep: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='SET NULL'), nullable=True)
    assistant_rep: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='SET NULL'), nullable=True)

    #Relationships
    students: Mapped[List['Students']] = relationship(back_populates='class_', foreign_keys='[Students.class_id]',
                                                      primaryjoin='Classes.id == Students.class_id')
    mentor: Mapped['Educator']= relationship(back_populates='mentored_class', foreign_keys='[Classes.mentor_id]')
    class_rep: Mapped['Students']= relationship(foreign_keys='[Classes.student_rep]')
    assist_rep: Mapped['Students']= relationship(foreign_keys='[Classes.assistant_rep]')


    __table_args__ = (
        UniqueConstraint('level', 'code', name='uq_class_level_code'),
        Index('idx_class_level_code', 'level', 'code')
    )

    def __repr__(self) -> str:
        return f"Class(level={self.level}, code={self.code}, mentor={self.mentor_id})"



class Departments(Base, AuditMixins, TimeStampMixins, ArchiveMixins):
    """
   Represents a department within an educational institution, including its name, code,
   description, and associated mentor. Links to students and educator mentor relationships.

   Inherits from Base, AuditMixins, TimeStampMixins, and ArchiveMixins.
   """
    __tablename__ = 'departments'

    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    name: Mapped[DepartmentName] = mapped_column(Enum(DepartmentName, name = 'departmentname'))
    code: Mapped[DepartmentCode] = mapped_column(Enum(DepartmentCode, name = 'departmentcode'))
    description: Mapped[str] = mapped_column(String(500))
    mentor_id: Mapped[UUID] = mapped_column(ForeignKey('educator.id', ondelete='RESTRICT'))

    #Relationships
    students:Mapped[List['Students']] = relationship(back_populates='department')
    mentor:Mapped['Educator'] = relationship(back_populates='mentored_department', foreign_keys='[Departments.mentor_id]')



class StaffDepartments(Base, AuditMixins, TimeStampMixins, ArchiveMixins):
    """
    Represents a staff department, including its name, description, and manager.
    Links to the staff member who manages the department.
    Inherits from Base, AuditMixins, TimeStampMixins, and ArchiveMixins.
    """
    __tablename__ = 'staff_departments'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    name: Mapped[StaffDepartmentName] = mapped_column(Enum(StaffDepartmentName, name='staffdepartmentname',unique=True))
    description: Mapped[str] = mapped_column(String(500))
    manager_id: Mapped[UUID] = mapped_column(ForeignKey('staff.id',ondelete='SET NULL'), nullable = True)

    #Relationships
    manager: Mapped['Staff'] = relationship(foreign_keys = '[StaffDepartments.manager_id]')


class StaffRoles(Base, AuditMixins, TimeStampMixins, ArchiveMixins):
    """
     Represents a role assigned to a staff member, including the role name and description.
     Inherits from Base, AuditMixins, TimeStampMixins, and ArchiveMixins.
    """
    __tablename__ = 'staff_roles'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(500))