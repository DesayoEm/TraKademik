"""Modified grade type and accesslevel enums

Revision ID: 39dc638b0954
Revises: 2f264d4baf72
Create Date: 2025-01-20 19:17:17.759590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from V2.app.database.models.common_imports import Base


# revision identifiers, used by Alembic.
revision: str = '39dc638b0954'
down_revision: Union[str, None] = '2f264d4baf72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grades', 'type')
    op.drop_column('students', 'access_level')
    op.drop_column('parents', 'access_level')
    op.drop_column('staff', 'access_level')
    op.drop_column('users', 'access_level')
    op.drop_column('access_level_changes', 'previous_level')
    op.drop_column('access_level_changes', 'new_level')

    op.execute("DROP TYPE gradetype;")
    op.execute("DROP TYPE accesslevel;")

    op.execute("""CREATE TYPE gradetype AS ENUM ('EXAM', 'TEST', 'ASSIGNMENT', 'PRACTICALS', 'MOCKEXAM', 'EXTRACURRICULAR');""")
    op.execute("""CREATE TYPE accesslevel AS ENUM ('USER', 'ADMIN', 'SUPERUSER', 'SUPERADMIN');""")

    op.add_column('grades', sa.Column('type',
                                        postgresql.ENUM('EXAM', 'TEST', 'ASSIGNMENT', 'PRACTICALS', 'MOCKEXAM', 'EXTRACURRICULAR',
                                        name='gradetype'),
                                        autoincrement=False, nullable=False))

    op.add_column('users', sa.Column('access_level',
                                      postgresql.ENUM('USER', 'ADMIN', 'SUPERUSER', 'SUPERADMIN',
                                                      name='accesslevel'),
                                      autoincrement=False, nullable=False))

    op.add_column('access_level_changes', sa.Column('previous_level',
                                        postgresql.ENUM('USER', 'ADMIN', 'SUPERUSER', 'SUPERADMIN',
                                                        name='accesslevel'),
                                        autoincrement=False, nullable=False))

    op.add_column('access_level_changes', sa.Column('new_level',
                                                    postgresql.ENUM('USER', 'ADMIN', 'SUPERUSER', 'SUPERADMIN',
                                                                    name='accesslevel'),
                                                    autoincrement=False, nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
