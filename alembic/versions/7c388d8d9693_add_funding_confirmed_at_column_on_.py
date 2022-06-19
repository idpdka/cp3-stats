"""add funding_confirmed_at column on tenants

Revision ID: 7c388d8d9693
Revises: 5175b55d1af8
Create Date: 2022-06-19 10:40:28.982959+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c388d8d9693'
down_revision = '5175b55d1af8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('unit', sa.Column('funding_confirmed_at', sa.DateTime))


def downgrade():
    op.drop_column('unit', 'funding_confirmed_at')
