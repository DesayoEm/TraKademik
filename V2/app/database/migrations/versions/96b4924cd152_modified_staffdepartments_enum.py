"""Modified StaffDepartments Enum

Revision ID: 96b4924cd152
Revises: f27745be0346
Create Date: 2025-01-22 06:29:22.114859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from V2.app.database.models.common_imports import Base
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '96b4924cd152'
down_revision: Union[str, None] = 'f27745be0346'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TYPE staffdepartmentname RENAME TO old_staffdepartmentname")
    op.execute("CREATE TYPE staffdepartmentname AS ENUM ('Admin', 'Education', 'Operations', 'Support', 'System', 'Other')")
    op.execute("ALTER TABLE staff_departments ALTER COLUMN name TYPE staffdepartmentname USING name::text::staffdepartmentname")
    op.execute("DROP TYPE old_staffdepartmentname")

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
