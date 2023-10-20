"""Fix Mapped

Revision ID: 37d01fae310e
Revises: b48dd77d8f75
Create Date: 2023-10-19 11:19:58.067284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37d01fae310e'
down_revision: Union[str, None] = 'b48dd77d8f75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.create_unique_constraint(None, 'user', ['email'])
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_verified')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###