"""add is_inhabited column on tenants

Revision ID: 5175b55d1af8
Revises: a14db07546e4
Create Date: 2022-06-19 08:28:27.061505+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5175b55d1af8'
down_revision = 'a14db07546e4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('unit', sa.Column('is_inhabited', sa.Integer, nullable=False))


def downgrade():
    op.drop_column('unit', 'is_inhabited')
