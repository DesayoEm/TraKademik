from .common_imports import *
from .data_enums import (ClassLevel, Term, ApprovalStatus, SubjectGroup, GradeType, DepartmentName)
from .mixins import AuditMixins, SoftDeleteMixins, TimeStampMixins

class Subjects(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
    Represents an educational subject with attributes like name, class level,
    department, and compulsory status. Includes relationships to grades, students,
    and educators.

    Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
    """
    __tablename__ = 'subjects'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    name: Mapped[str] = mapped_column(String(30))
    class_level: Mapped[ClassLevel] = mapped_column(Enum(ClassLevel))
    group: Mapped[SubjectGroup] = mapped_column(Enum(SubjectGroup), nullable = True)
    is_elective: Mapped[bool] = mapped_column(default = True)

    #Relationships
    grades = relationship('Grades', back_populates='subject')
    total_grades = relationship('TotalGrades', back_populates='subject')
    student_subjects = relationship('StudentSubjects', back_populates='subject')
    educators = relationship('EducatorSubjects', back_populates='subject')



class Grades(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
    Represents student grades, linking students, subjects, departments, and educators.
    Includes attributes for academic year, term, grade type, and marks, with optional file URL.

    Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
    """
    __tablename__ = 'grades'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subjects.id', ondelete='SET NULL'), nullable=True)
    department_id: Mapped[UUID] = mapped_column(ForeignKey('departments.id', ondelete='SET NULL'), nullable=True)
    academic_year: Mapped[int] = mapped_column(Integer)
    term: Mapped[Term] = mapped_column(Enum(Term))
    type: Mapped[GradeType] = mapped_column(Enum(GradeType))
    marks: Mapped[int] = mapped_column(Integer)
    file_url: Mapped[str] = mapped_column(String(300), nullable = True)
    remarks: Mapped[str] = mapped_column(String(300), nullable = True)
    graded_by: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SET NULL'))

    #Relationships
    subject = relationship('Subjects', back_populates='grades', foreign_keys='[Grades.subject_id]')
    student = relationship('Students', back_populates='grades', foreign_keys='[Grades.student_id]')
    grader = relationship('Educator', foreign_keys="[Grades.graded_by]")
    department = relationship('Departments', foreign_keys="[Grades.department_id]")


    __table_args__ = (
        Index('idx_subject_id', 'subject_id'),
        Index('idx_marks', 'marks'),
        Index('idx_graded_by', 'graded_by'),
        Index('idx_grade_academic_year', 'academic_year')
    )


class TotalGrades(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
   Represents total grades for a student in a subject, including total marks, rank,
   academic year, and term. Links students and subjects with unique constraints on
   student, subject, academic year, and term.

   Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
   """
    __tablename__ = 'total_grades'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subjects.id', ondelete='SET NULL'))
    academic_year: Mapped[int] = mapped_column(Integer)
    term: Mapped[Term] = mapped_column(Enum(Term))
    total_marks: Mapped[float] = mapped_column(Float)
    rank: Mapped[Optional[int]] = mapped_column(Integer, nullable = True)

    #Relationships
    student = relationship('Students', back_populates='total_grades', foreign_keys='[TotalGrades.student_id]')
    subject = relationship('Subjects', back_populates='total_grades', foreign_keys='[TotalGrades.subject_id]')


    __table_args__ = (
        UniqueConstraint('student_id', 'subject_id', 'academic_year', 'term'),
        Index('idx_total_grade_subject_id', 'id'),
        Index('idx_total_marks', 'total_marks'),
        Index('idx_total_grade_academic_year', 'academic_year')
    )



class StudentSubjects(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
   Represents a student's enrollment in a subject for a specific academic year and term.
   Includes attributes like enrollment status and subject title.

   Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
   """
    __tablename__ = 'student_subjects'

    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subjects.id', ondelete='SET NULL'))
    academic_year: Mapped[int] = mapped_column(Integer)
    term: Mapped[Term] = mapped_column(Enum(Term))
    is_active: Mapped[bool] = mapped_column(Boolean, default = True)
    title: Mapped[str] = mapped_column(String(50))

    #Relationships
    subject = relationship('Subjects', back_populates='student_subjects', foreign_keys='[StudentSubjects.subject_id]')
    student = relationship('Students', back_populates='subjects_taken', foreign_keys='[StudentSubjects.student_id]')


class EducatorSubjects(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
    Represents an educator's assignment to a subject for a specific academic year and term.
    Includes attributes like active status and term.

    Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
    """
    __tablename__ = 'educator_subjects'

    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    educator_id: Mapped[UUID] = mapped_column(ForeignKey('educator.id', ondelete='SET NULL'))
    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subjects.id', ondelete='SET NULL'), nullable=True)
    term: Mapped[Term] = mapped_column(Enum(Term))
    academic_year: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default = False)

    #Relationships
    educator = relationship('Educator', back_populates='subjects_taken', foreign_keys="[EducatorSubjects.educator_id]")
    subject = relationship("Subjects", back_populates="educators", foreign_keys="[EducatorSubjects.subject_id]")



class Repetitions(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
     Represents a student's repetition of a class, including details like class level change,
     reason for repetition, approval status, and class assignments.

     Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
     """
    __tablename__ = 'repetitions'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    academic_year: Mapped[int] = mapped_column(Integer)
    from_class_level: Mapped[ClassLevel] = mapped_column(Enum(ClassLevel))
    to_class_level: Mapped[ClassLevel] = mapped_column(Enum(ClassLevel))
    from_class_id: Mapped[UUID] = mapped_column(ForeignKey ('classes.id',ondelete='SET NULL'),nullable=True)
    to_class_id: Mapped[UUID] = mapped_column(ForeignKey ('classes.id', ondelete='SET NULL'),nullable=True)
    reason: Mapped[str] = mapped_column(String(500))
    status: Mapped[ApprovalStatus] = mapped_column(Enum(ApprovalStatus), default=ApprovalStatus.PENDING)
    status_updated_by: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SET NULL'), nullable=True)
    status_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    rejection_reason: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    #Relationships
    repeater = relationship('Students', back_populates='classes_repeated', foreign_keys='[Repetitions.student_id]')
    from_class = relationship('Classes', foreign_keys='[Repetitions.from_class_id]')
    to_class = relationship('Classes', foreign_keys='[Repetitions.to_class_id]')
    status_updated_staff = relationship('Staff', foreign_keys='[Repetitions.status_updated_by]')

    __table_args__ = (
        Index('idx_repetition_status', 'status'),
        Index('idx_student_status', 'student_id', 'status'),
        Index('idx_student_academic_year', 'student_id', 'academic_year'),
        Index('idx_from_class', 'from_class_id'),
        Index('idx_to_class', 'to_class_id'),
    )

    def __repr__(self) -> str:
        return f"student {self.student_id} repetition in {self.academic_year} was actioned by {self.status_updated_staff}"


class StudentTransfers(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
   Represents a student's transfer between departments or class levels, including the reason,
   approval status, and status updates.

   Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
   """
    __tablename__ = 'student_transfers'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    academic_year: Mapped[int] = mapped_column(Integer)
    from_class_level: Mapped[ClassLevel] = mapped_column(Enum(ClassLevel))
    to_class_level: Mapped[ClassLevel] = mapped_column(Enum(ClassLevel))
    from_department_id: Mapped[UUID] = mapped_column(ForeignKey('departments.id', ondelete='RESTRICT'))
    to_department_id: Mapped[UUID] = mapped_column(ForeignKey('departments.id', ondelete='RESTRICT'))
    reason: Mapped[str] = mapped_column(String(500))
    status: Mapped[ApprovalStatus] = mapped_column(Enum(ApprovalStatus), default=ApprovalStatus.PENDING)
    status_updated_by: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SET NULL'))
    status_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    rejection_reason: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    #Relationships
    transferred_student = relationship('Students', back_populates='transfers',
                                       foreign_keys='[StudentTransfers.student_id]')
    from_dept = relationship('Departments', foreign_keys='[StudentTransfers.from_department_id]')
    to_dept = relationship('Departments', foreign_keys='[StudentTransfers.to_department_id]')
    status_updater = relationship('Staff', foreign_keys='[StudentTransfers.status_updated_by]')

    __table_args__ = (
        Index('idx_transfer_status', 'status'),
        Index('idx_student_transfer_status', 'student_id', 'status'),
        Index('idx_student-transfer_academic_year', 'student_id', 'academic_year'),
        Index('idx_from_department_id', 'from_department_id'),
        Index('idx_to_department_id', 'to_department_id'),
    )

    def __repr__(self) -> str:
        return f"student {self.student_id} transfer from {self.from_department_id} to {self.to_department_id} in {self.academic_year}\
        was actioned by {self.status_updater}"

class EducatorQualifications(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    """
    Represents an educator's assignment to a subject for a specific academic year and term.
    Includes attributes like active status and term.

    Inherits from Base, AuditMixins, TimeStampMixins, and SoftDeleteMixins.
    """
    __tablename__ = 'educator_qualifications'

    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    educator_id: Mapped[UUID] = mapped_column(ForeignKey('educator.id', ondelete='CASCADE'))

    #Relationships
    educator = relationship('Educator', back_populates='qualifications', foreign_keys="[EducatorQualifications.educator_id]")

