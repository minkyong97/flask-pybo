"""empty message

Revision ID: 2771cd4b3d8b
Revises: f7a79d1881cf
Create Date: 2020-10-07 19:10:07.321975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2771cd4b3d8b'
down_revision = 'f7a79d1881cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_answer_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_answer_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###