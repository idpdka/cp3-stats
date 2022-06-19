"""add subcomplex table

Revision ID: a14db07546e4
Revises: e3749f05595a
Create Date: 2022-06-19 13:29:32.533853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a14db07546e4'
down_revision = 'e3749f05595a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'subcomplex',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('code', sa.String(50)),
        sa.Column('address', sa.String(200)),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('deleted_at', sa.DateTime),
    )


def downgrade():
    op.drop_table('subcomplex')
