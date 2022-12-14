"""empty message

Revision ID: 10256989e6a9
Revises: 90ba4c7e4670
Create Date: 2022-11-18 11:56:46.769680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10256989e6a9'
down_revision = '90ba4c7e4670'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.create_index('ix_users_email', ['email'], unique=False)

    # ### end Alembic commands ###
