"""empty message

Revision ID: 83b6ba1af540
Revises: ebda05acce73
Create Date: 2018-11-26 11:42:51.679642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83b6ba1af540'
down_revision = 'ebda05acce73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model', sa.Column('preferred_map_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('model', 'preferred_map_id')
    # ### end Alembic commands ###