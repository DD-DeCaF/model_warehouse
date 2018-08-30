"""empty message

Revision ID: 1a664fb50066
Revises: 
Create Date: 2018-08-29 12:38:42.852124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a664fb50066'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('model_serialized', sa.JSON(), nullable=False),
    sa.Column('organism_id', sa.String(length=256), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('default_biomass_reaction', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model')
    # ### end Alembic commands ###
