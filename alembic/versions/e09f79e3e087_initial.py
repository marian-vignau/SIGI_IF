"""initial

Revision ID: e09f79e3e087
Revises: 
Create Date: 2019-04-05 10:06:51.831918

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e09f79e3e087'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('TableEscrito', sa.Column('observaciones', sa.Text))


def downgrade():
    op.drop_column('TableEscrito', 'observaciones')
