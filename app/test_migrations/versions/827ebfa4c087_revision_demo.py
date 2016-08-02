"""revision_demo

Revision ID: 827ebfa4c087
Revises: 
Create Date: 2016-08-02 19:52:53.110392

"""

# revision identifiers, used by Alembic.
revision = '827ebfa4c087'
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