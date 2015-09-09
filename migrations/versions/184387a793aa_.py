"""empty message

Revision ID: 184387a793aa
Revises: None
Create Date: 2015-09-08 21:11:06.607009

"""

# revision identifiers, used by Alembic.
revision = '184387a793aa'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('package',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('package')
    ### end Alembic commands ###