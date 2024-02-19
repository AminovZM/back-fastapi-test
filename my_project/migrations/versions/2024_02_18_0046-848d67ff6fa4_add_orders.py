"""Add orders

Revision ID: 848d67ff6fa4
Revises: 64dbe9e2f03b
Create Date: 2024-02-18 00:46:28.311682

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '848d67ff6fa4'
down_revision = '64dbe9e2f03b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_orders', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###
