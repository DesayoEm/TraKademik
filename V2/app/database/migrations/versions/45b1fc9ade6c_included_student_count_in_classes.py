"""Included student_count in classes

Revision ID: 45b1fc9ade6c
Revises: 9131957c66d6
Create Date: 2025-01-19 19:51:35.950367

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from V2.app.database.models.common_imports import Base
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '45b1fc9ade6c'
down_revision: Union[str, None] = '9131957c66d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('classes', sa.Column('student_count', sa.Integer(), nullable=False))

    op.execute("""CREATE TYPE departmentname AS ENUM ('SCIENCE', 'HUMANITIES', 'BUSINESS');""")

    op.alter_column('departments', 'name',
               existing_type=postgresql.ENUM('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmenttype'),
               type_=sa.Enum('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmentname'),
               existing_nullable=False, postgresql_using='departments::text::departmentname')


    op.drop_index('idx_staff_type', table_name='staff')

    op.alter_column('student_transfers', 'from_department',
               existing_type=postgresql.ENUM('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmenttype'),
               type_=sa.Enum('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmentname'),
               existing_nullable=False, postgresql_using='student_transfers::text::departmentname')

    op.alter_column('student_transfers', 'to_department',
               existing_type=postgresql.ENUM('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmenttype'),
               type_=sa.Enum('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmentname'),
               existing_nullable=False,
                    postgresql_using='student_transfers::text::departmentname')

    op.execute("DROP TYPE departmenttype;")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('student_transfers', 'to_department',
               existing_type=sa.Enum('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmentname'),
               type_=postgresql.ENUM('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmenttype'),
               existing_nullable=False)
    op.alter_column('student_transfers', 'from_department',
               existing_type=sa.Enum('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmentname'),
               type_=postgresql.ENUM('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmenttype'),
               existing_nullable=False)
    op.create_index('idx_staff_type', 'staff', ['staff_type'], unique=False)
    op.alter_column('departments', 'name',
               existing_type=sa.Enum('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmentname'),
               type_=postgresql.ENUM('SCIENCE', 'HUMANITIES', 'BUSINESS', name='departmenttype'),
               existing_nullable=False)
    op.drop_column('classes', 'student_count')
    # ### end Alembic commands ###
