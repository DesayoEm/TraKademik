from .common_imports import *
from app.database.models.data_enums import (
        ClassLevel, Term, ApprovalStatus, SubjectDepartmentType,
        GradeType)

from mixins import AuditMixins, SoftDeleteMixins, TimeStampMixins

class Subjects(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    __tablename__ = 'subjects'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    name: Mapped[str] = mapped_column(String(30))
    class_level: Mapped[ClassLevel] = mapped_column(Enum(ClassLevel))
    department_type: Mapped[SubjectDepartmentType] = mapped_column(Enum(SubjectDepartmentType))
    is_compulsory: Mapped[bool] = mapped_column(default = True)

    #Relationships
    student = relationship('Students', back_populates='subjects_taken')
    grades = relationship('Grades', back_populates='subject')
    total_grades = relationship('TotalGrades', back_populates='subject')
    student_subjects = relationship('StudentSubjects', back_populates='subject')
    educators = relationship('EducatorSubjects', back_populates='subject')



class Grades(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
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
    graded_by: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SETT NULL'))

    #Relationships
    subject = relationship('Subjects', back_populates='grades')
    student = relationship('Students', back_populates='grades')
    grader = relationship('Staff', foreign_keys=[graded_by])
    department = relationship('Department', foreign_keys=[department_id])


    __table_args__ = (
        Index('idx_subject_id', 'subject_id'),
        Index('idx_marks', 'marks'),
        Index('idx_graded_by', 'graded_by'),
        Index('idx_grade_academic_year', 'academic_year')
    )


class TotalGrades(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    __tablename__ = 'total_grades'
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subjects.id', ondelete='SET NULL'))
    academic_year: Mapped[int] = mapped_column(Integer)
    term: Mapped[Term] = mapped_column(Enum(Term))
    total_marks: Mapped[float] = mapped_column(Float)
    rank: Mapped[Optional[int]] = mapped_column(Integer, nullable = True)

    #Relationships
    student = relationship('Students', back_populates='total_grades')
    subject = relationship('Subjects', back_populates='total_grades')


    __table_args__ = (
        UniqueConstraint('student_id', 'subject_id', 'academic_year', 'term'),
        Index('idx_total_grade_subject_id', 'id'),
        Index('idx_total_marks', 'total_marks'),
        Index('idx_total_grade_academic_year', 'academic_year')
    )



class StudentSubjects(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    __tablename__ = 'student_subjects'

    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subjects.id', ondelete='SET NULL'))
    academic_year: Mapped[int] = mapped_column(Integer)
    term: Mapped[Term] = mapped_column(Enum(Term))
    is_active: Mapped[bool] = mapped_column(Boolean, default = True)
    title: Mapped[str] = mapped_column(String(50))

    #Relationships
    subject = relationship('Subjects', back_populates='student_subjects')
    student = relationship('Students', back_populates='subjects_taken')


class EducatorSubjects(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    __tablename__ = 'educator_subjects'

    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    educator_id: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SET NULL'))
    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subjects.id', ondelete='SET NULL'), nullable=True)
    term: Mapped[Term] = mapped_column(Enum(Term))
    academic_year: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default = False)

    #Relationships
    educator = relationship('Educator', back_populates='subjects_taken')
    subject = relationship("Subjects", back_populates="educators")


class Repetitions(Base, AuditMixins, TimeStampMixins, SoftDeleteMixins):
    __tablename__ = 'repetitions'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    academic_year: Mapped[int] = mapped_column(Integer)
    from_class_level: Mapped[ClassLevel] = mapped_column(ForeignKey ('classes.level', ondelete='SET NULL'))
    to_class_level: Mapped[ClassLevel] = mapped_column(ForeignKey ('classes.level',ondelete='SET NULL'))
    from_class_id: Mapped[UUID] = mapped_column(ForeignKey ('classes.id',ondelete='SET NULL'))
    to_class_id: Mapped[UUID] = mapped_column(ForeignKey ('classes.id', ondelete='SET NULL'))
    reason: Mapped[str] = mapped_column(String(500))
    status: Mapped[ApprovalStatus] = mapped_column(Enum(ApprovalStatus), default=ApprovalStatus.PENDING)
    status_updated_by: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SET NULL'))
    status_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    rejection_reason: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    #Relationships
    repeater = relationship('Students', back_populates='classes_repeated')
    from_class = relationship('Classes', foreign_keys=[from_class_id])
    to_class = relationship('Classes', foreign_keys=[to_class_id])
    status_updated_staff = relationship('Staff', foreign_keys=[status_updated_by])

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
    __tablename__ = 'student_transfers'
    id: Mapped[UUID]  = mapped_column(UUID(as_uuid = True), primary_key= True, default = uuid4)
    student_id: Mapped[UUID] = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))
    academic_year: Mapped[int] = mapped_column(Integer)

    from_class_level: Mapped[ClassLevel] = mapped_column(ForeignKey ('classes.level', ondelete='SET NULL'))
    to_class_level: Mapped[ClassLevel] = mapped_column(ForeignKey ('classes.level', ondelete='SET NULL'))
    from_department: Mapped[UUID] = mapped_column(ForeignKey ('departments.id', ondelete='SET NULL'))
    to_department: Mapped[UUID] = mapped_column(ForeignKey ('departments.id', ondelete='SET NULL'))
    reason: Mapped[str] = mapped_column(String(500))
    status: Mapped[ApprovalStatus] = mapped_column(Enum(ApprovalStatus), default=ApprovalStatus.PENDING)
    status_updated_by: Mapped[UUID] = mapped_column(ForeignKey('staff.id', ondelete='SET NULL'))
    status_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    rejection_reason: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    #Relationships
    transferred_student = relationship('Students', back_populates='transfers')
    from_dept = relationship('Department', foreign_keys=[from_department])
    to_dept = relationship('Department', foreign_keys=[to_department])
    status_updater = relationship('Staff', foreign_keys=[status_updated_by])

    __table_args__ = (
        Index('idx_transfer_status', 'status'),
        Index('idx_student_transfer_status', 'student_id', 'status'),
        Index('idx_student-transfer_academic_year', 'student_id', 'academic_year'),
        Index('idx_from_department', 'from_department'),
        Index('idx_to_department', 'to_department'),
    )

    def __repr__(self) -> str:
        return f"student {self.student_id} transfer from {self.from_department} to {self.to_department} in {self.academic_year}\
        was actioned by {self.status_updater}"