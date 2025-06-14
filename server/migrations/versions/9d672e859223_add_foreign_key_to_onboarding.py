"""add foreign key to onboarding

Revision ID: 9d672e859223
Revises: a387cb71b55a
Create Date: 2025-06-14 23:53:02.248763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d672e859223'
down_revision = 'a387cb71b55a'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode to safely alter tables in SQLite
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            op.f('fk_onboardings_employee_id_employees'),
            'employees',
            ['employee_id'],
            ['id']
        )

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.create_foreign_key(
            op.f('fk_reviews_employee_id_employees'),
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(op.f('fk_reviews_employee_id_employees'), type_='foreignkey')

    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')