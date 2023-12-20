"""discussion table

Revision ID: f1be77b0f510
Revises: 0a593b0a294c
Create Date: 2023-12-20 19:36:33.430260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1be77b0f510'
down_revision = '0a593b0a294c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_admin_id'), ['id'])
        batch_op.create_unique_constraint(batch_op.f('uq_admin_login'), ['login'])

    with op.batch_alter_table('case', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_case_name'), ['name'])

    with op.batch_alter_table('service', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.TEXT(length=60),
               type_=sa.String(length=60),
               existing_nullable=False)
        batch_op.alter_column('image',
               existing_type=sa.TEXT(length=20),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.TEXT(length=120),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('essence',
               existing_type=sa.TEXT(length=120),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('development_stages',
               existing_type=sa.TEXT(length=120),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('cost_description',
               existing_type=sa.TEXT(length=120),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('cost',
               existing_type=sa.TEXT(length=20),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('demand',
               existing_type=sa.TEXT(length=120),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.create_unique_constraint(batch_op.f('uq_service_name'), ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('service', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_service_name'), type_='unique')
        batch_op.alter_column('demand',
               existing_type=sa.String(length=120),
               type_=sa.TEXT(length=120),
               existing_nullable=False)
        batch_op.alter_column('cost',
               existing_type=sa.String(length=20),
               type_=sa.TEXT(length=20),
               existing_nullable=False)
        batch_op.alter_column('cost_description',
               existing_type=sa.String(length=120),
               type_=sa.TEXT(length=120),
               existing_nullable=False)
        batch_op.alter_column('development_stages',
               existing_type=sa.String(length=120),
               type_=sa.TEXT(length=120),
               existing_nullable=False)
        batch_op.alter_column('essence',
               existing_type=sa.String(length=120),
               type_=sa.TEXT(length=120),
               existing_nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.String(length=120),
               type_=sa.TEXT(length=120),
               existing_nullable=False)
        batch_op.alter_column('image',
               existing_type=sa.String(length=20),
               type_=sa.TEXT(length=20),
               existing_nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.String(length=60),
               type_=sa.TEXT(length=60),
               existing_nullable=False)

    with op.batch_alter_table('case', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_case_name'), type_='unique')

    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_admin_login'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_admin_id'), type_='unique')

    # ### end Alembic commands ###
