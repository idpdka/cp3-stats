"""add unit table

Revision ID: e3749f05595a
Revises: 
Create Date: 2022-06-19 13:25:17.474110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3749f05595a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'unit',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('subcomplex_id', sa.Integer),
        sa.Column('owner_name', sa.String(100)),
        sa.Column('co_owner_name', sa.String(100)),
        sa.Column('unit_no', sa.Integer),
        sa.Column('phone_no', sa.String(20)),
        sa.Column('email', sa.String(50)),
        sa.Column('handover_satisfaction', sa.Float),
        sa.Column('handover_at', sa.DateTime),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('deleted_at', sa.DateTime),
    )


def downgrade():
    op.drop_table('unit')
