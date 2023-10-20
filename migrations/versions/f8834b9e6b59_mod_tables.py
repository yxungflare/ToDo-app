"""Mod tables

Revision ID: f8834b9e6b59
Revises: 4ab68d41acb9
Create Date: 2023-10-18 15:19:36.246269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8834b9e6b59'
down_revision: Union[str, None] = '4ab68d41acb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'role', ['id'])
    op.add_column('user', sa.Column('phone_number', sa.String(length=12), nullable=False))
    op.add_column('user', sa.Column('hashed_password', sa.String(length=1024), nullable=False))
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_verified', sa.Boolean(), nullable=False))
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    op.create_unique_constraint(None, 'user', ['id'])
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=1024), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_column('user', 'is_verified')
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'hashed_password')
    op.drop_column('user', 'phone_number')
    op.drop_constraint(None, 'role', type_='unique')
    # ### end Alembic commands ###