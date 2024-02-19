"""Add to basket row id_user

Revision ID: a7a4eddb2b35
Revises: 68d0fc989bee
Create Date: 2024-02-17 06:25:40.066778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7a4eddb2b35'
down_revision = '68d0fc989bee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('basket', sa.Column('id_user', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('basket', 'id_user')
    # ### end Alembic commands ###
