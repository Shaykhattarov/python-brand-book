"""discussion table

Revision ID: 0b918afd9c4e
Revises: f1be77b0f510
Create Date: 2023-12-20 19:37:30.682307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b918afd9c4e'
down_revision = 'f1be77b0f510'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discussion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('phone', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_discussion'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('discussion')
    # ### end Alembic commands ###