"""tables

Revision ID: 0084e8456ed5
Revises: 
Create Date: 2022-09-16 00:06:54.490843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0084e8456ed5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('developer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('story',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('story_name', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('estimated_points', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task',
    sa.Column('task_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('story_id', sa.Integer(), nullable=True),
    sa.Column('task_name', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('estimated_points', sa.Integer(), nullable=True),
    sa.Column('developer_id', sa.Integer(), nullable=True),
    sa.Column('iteration', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['developer_id'], ['developer.id'], ),
    sa.ForeignKeyConstraint(['story_id'], ['story.id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.create_table('task_actual_times',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('actual_time', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['task.task_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task_actual_times')
    op.drop_table('task')
    op.drop_table('story')
    op.drop_table('developer')
    # ### end Alembic commands ###