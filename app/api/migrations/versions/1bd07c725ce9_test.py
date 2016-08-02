"""test

Revision ID: 1bd07c725ce9
Revises: 
Create Date: 2016-08-02 11:08:12.123723

"""

# revision identifiers, used by Alembic.
revision = '1bd07c725ce9'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('guid', sa.String(), unique=True, nullable=False),
        sa.Column('email', sa.String(), unique=True),
        sa.Column('password', sa.String(), unique=True)
    )


def downgrade():
    op.drop_table('User')

