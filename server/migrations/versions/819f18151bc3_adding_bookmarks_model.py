"""adding bookmarks model

Revision ID: 819f18151bc3
Revises: 9cd40f010ea1
Create Date: 2025-03-01 17:36:34.228876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '819f18151bc3'
down_revision = '9cd40f010ea1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookmarks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['record_id'], ['records.id'], name=op.f('fk_bookmarks_record_id_records')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_bookmarks_user_id_users')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'record_id', name='_user_record_uc_bookmarks')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookmarks')
    # ### end Alembic commands ###
