"""rename address

Revision ID: f02617d87f64
Revises: b7f92d26d553
Create Date: 2025-06-13 14:28:28.167857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f02617d87f64'
down_revision = 'b7f92d26d553'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
 op.alter_column('departments', 'address',  new_column_name='location')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
 op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
