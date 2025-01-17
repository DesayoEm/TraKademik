"""Included foreign keys

Revision ID: ec89d7e19bf8
Revises: 00b8cc36b9e4
Create Date: 2025-01-17 23:53:17.027872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.database.models.common_imports import Base


# revision identifiers, used by Alembic.
revision: str = 'ec89d7e19bf8'
down_revision: Union[str, None] = '00b8cc36b9e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'access_level_changes', 'users', ['profile_id'], ['profile_id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'access_level_changes', 'staff', ['changed_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'admin', 'staff', ['id'], ['id'])
    op.alter_column('classes', 'mentor_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('classes', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('classes', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('classes', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'classes', 'educator', ['mentor_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'classes', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'classes', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'classes', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'commercial', 'staff', ['id'], ['id'])
    op.alter_column('departments', 'mentor_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('departments', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('departments', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('departments', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'departments', 'educator', ['mentor_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'departments', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'departments', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'departments', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'educator', 'staff', ['id'], ['id'])
    op.alter_column('educator_subjects', 'subject_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('educator_subjects', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('educator_subjects', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('educator_subjects', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'educator_subjects', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'educator_subjects', 'subjects', ['subject_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'educator_subjects', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'educator_subjects', 'educator', ['educator_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'educator_subjects', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.alter_column('grades', 'subject_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('grades', 'department_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('grades', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('grades', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('grades', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'grades', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'grades', 'departments', ['department_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'grades', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'grades', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'grades', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'grades', 'subjects', ['subject_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'grades', 'staff', ['graded_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'management', 'staff', ['id'], ['id'])
    op.alter_column('parents', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('parents', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('parents', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_unique_constraint(None, 'parents', ['profile_id'])
    op.create_foreign_key(None, 'parents', 'users', ['profile_id'], ['profile_id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'parents', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'parents', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'parents', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.alter_column('repetitions', 'from_class_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('repetitions', 'to_class_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('repetitions', 'status_updated_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('repetitions', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('repetitions', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('repetitions', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'repetitions', 'classes', ['to_class_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'repetitions', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'repetitions', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'repetitions', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'repetitions', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'repetitions', 'staff', ['status_updated_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'repetitions', 'classes', ['from_class_id'], ['id'], ondelete='SET NULL')
    op.alter_column('staff', 'department_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('staff', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('staff', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_unique_constraint(None, 'staff', ['profile_id'])
    op.create_foreign_key(None, 'staff', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff', 'staff_departments', ['department_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'staff', 'users', ['profile_id'], ['profile_id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'staff', 'staff_roles', ['role_id'], ['id'], ondelete='CASCADE')
    op.alter_column('staff_departments', 'manager_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('staff_departments', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('staff_departments', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('staff_departments', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'staff_departments', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff_departments', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff_departments', 'staff', ['manager_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff_departments', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.alter_column('staff_roles', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('staff_roles', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('staff_roles', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'staff_roles', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff_roles', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'staff_roles', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.alter_column('student_documents', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('student_documents', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('student_documents', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'student_documents', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_documents', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_documents', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.alter_column('student_subjects', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('student_subjects', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('student_subjects', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'student_subjects', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_subjects', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_subjects', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'student_subjects', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_subjects', 'subjects', ['subject_id'], ['id'], ondelete='SET NULL')
    op.alter_column('student_transfers', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('student_transfers', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('student_transfers', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'student_transfers', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_transfers', 'staff', ['status_updated_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_transfers', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_transfers', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'student_transfers', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.alter_column('students', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('students', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('students', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_index('idx_students_profile_id', 'students', ['profile_id'], unique=False)
    op.create_index('idx_students_soft_deleted_at', 'students', ['soft_deleted_at'], unique=False)
    op.create_unique_constraint(None, 'students', ['profile_id'])
    op.create_foreign_key(None, 'students', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'students', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'students', 'parents', ['parent_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'students', 'departments', ['department_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'students', 'users', ['profile_id'], ['profile_id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'students', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'students', 'classes', ['class_id'], ['id'], ondelete='RESTRICT')
    op.alter_column('subjects', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('subjects', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('subjects', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'subjects', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'subjects', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'subjects', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'support', 'staff', ['id'], ['id'])
    op.alter_column('total_grades', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('total_grades', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('total_grades', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'total_grades', 'students', ['student_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'total_grades', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'total_grades', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'total_grades', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'total_grades', 'subjects', ['subject_id'], ['id'], ondelete='SET NULL')
    op.alter_column('users', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('users', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('users', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=True)
    op.create_foreign_key(None, 'users', 'staff', ['last_modified_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'users', 'staff', ['soft_deleted_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'users', 'staff', ['created_by'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.alter_column('users', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('users', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('users', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'total_grades', type_='foreignkey')
    op.drop_constraint(None, 'total_grades', type_='foreignkey')
    op.drop_constraint(None, 'total_grades', type_='foreignkey')
    op.drop_constraint(None, 'total_grades', type_='foreignkey')
    op.drop_constraint(None, 'total_grades', type_='foreignkey')
    op.alter_column('total_grades', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('total_grades', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('total_grades', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'support', type_='foreignkey')
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.alter_column('subjects', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('subjects', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('subjects', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='foreignkey')
    op.drop_constraint(None, 'students', type_='unique')
    op.drop_index('idx_students_soft_deleted_at', table_name='students')
    op.drop_index('idx_students_profile_id', table_name='students')
    op.alter_column('students', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('students', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('students', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'student_transfers', type_='foreignkey')
    op.drop_constraint(None, 'student_transfers', type_='foreignkey')
    op.drop_constraint(None, 'student_transfers', type_='foreignkey')
    op.drop_constraint(None, 'student_transfers', type_='foreignkey')
    op.drop_constraint(None, 'student_transfers', type_='foreignkey')
    op.alter_column('student_transfers', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('student_transfers', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('student_transfers', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'student_subjects', type_='foreignkey')
    op.drop_constraint(None, 'student_subjects', type_='foreignkey')
    op.drop_constraint(None, 'student_subjects', type_='foreignkey')
    op.drop_constraint(None, 'student_subjects', type_='foreignkey')
    op.drop_constraint(None, 'student_subjects', type_='foreignkey')
    op.alter_column('student_subjects', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('student_subjects', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('student_subjects', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'student_documents', type_='foreignkey')
    op.drop_constraint(None, 'student_documents', type_='foreignkey')
    op.drop_constraint(None, 'student_documents', type_='foreignkey')
    op.alter_column('student_documents', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('student_documents', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('student_documents', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'staff_roles', type_='foreignkey')
    op.drop_constraint(None, 'staff_roles', type_='foreignkey')
    op.drop_constraint(None, 'staff_roles', type_='foreignkey')
    op.alter_column('staff_roles', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff_roles', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff_roles', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'staff_departments', type_='foreignkey')
    op.drop_constraint(None, 'staff_departments', type_='foreignkey')
    op.drop_constraint(None, 'staff_departments', type_='foreignkey')
    op.drop_constraint(None, 'staff_departments', type_='foreignkey')
    op.alter_column('staff_departments', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff_departments', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff_departments', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff_departments', 'manager_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='foreignkey')
    op.drop_constraint(None, 'staff', type_='unique')
    op.alter_column('staff', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('staff', 'department_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.drop_constraint(None, 'repetitions', type_='foreignkey')
    op.drop_constraint(None, 'repetitions', type_='foreignkey')
    op.drop_constraint(None, 'repetitions', type_='foreignkey')
    op.drop_constraint(None, 'repetitions', type_='foreignkey')
    op.drop_constraint(None, 'repetitions', type_='foreignkey')
    op.drop_constraint(None, 'repetitions', type_='foreignkey')
    op.drop_constraint(None, 'repetitions', type_='foreignkey')
    op.alter_column('repetitions', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('repetitions', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('repetitions', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('repetitions', 'status_updated_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('repetitions', 'to_class_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('repetitions', 'from_class_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'parents', type_='foreignkey')
    op.drop_constraint(None, 'parents', type_='foreignkey')
    op.drop_constraint(None, 'parents', type_='foreignkey')
    op.drop_constraint(None, 'parents', type_='foreignkey')
    op.drop_constraint(None, 'parents', type_='unique')
    op.alter_column('parents', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('parents', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('parents', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'management', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.drop_constraint(None, 'grades', type_='foreignkey')
    op.alter_column('grades', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('grades', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('grades', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('grades', 'department_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('grades', 'subject_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'educator_subjects', type_='foreignkey')
    op.drop_constraint(None, 'educator_subjects', type_='foreignkey')
    op.drop_constraint(None, 'educator_subjects', type_='foreignkey')
    op.drop_constraint(None, 'educator_subjects', type_='foreignkey')
    op.drop_constraint(None, 'educator_subjects', type_='foreignkey')
    op.alter_column('educator_subjects', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('educator_subjects', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('educator_subjects', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('educator_subjects', 'subject_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'educator', type_='foreignkey')
    op.drop_constraint(None, 'departments', type_='foreignkey')
    op.drop_constraint(None, 'departments', type_='foreignkey')
    op.drop_constraint(None, 'departments', type_='foreignkey')
    op.drop_constraint(None, 'departments', type_='foreignkey')
    op.alter_column('departments', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('departments', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('departments', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('departments', 'mentor_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'commercial', type_='foreignkey')
    op.drop_constraint(None, 'classes', type_='foreignkey')
    op.drop_constraint(None, 'classes', type_='foreignkey')
    op.drop_constraint(None, 'classes', type_='foreignkey')
    op.drop_constraint(None, 'classes', type_='foreignkey')
    op.alter_column('classes', 'soft_deleted_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('classes', 'last_modified_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('classes', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('classes', 'mentor_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.drop_constraint(None, 'admin', type_='foreignkey')
    op.drop_constraint(None, 'access_level_changes', type_='foreignkey')
    op.drop_constraint(None, 'access_level_changes', type_='foreignkey')
    # ### end Alembic commands ###
