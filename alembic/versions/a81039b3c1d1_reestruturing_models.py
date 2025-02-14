"""Reestruturing models

Revision ID: a81039b3c1d1
Revises: e71af4aa0d4d
Create Date: 2022-03-04 00:41:56.967980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a81039b3c1d1'
down_revision = 'e71af4aa0d4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('projects')
    op.drop_table('projecttags')
    op.drop_table('homecontents')
    op.drop_table('tagposts')
    op.drop_table('admins')
    op.drop_table('tags')
    op.drop_table('socials')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('socials',
    sa.Column('socialid', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('link', sa.VARCHAR(), nullable=False),
    sa.Column('media', sa.VARCHAR(), nullable=True),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('socialid')
    )
    op.create_table('tags',
    sa.Column('tagid', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('tagid')
    )
    op.create_table('admins',
    sa.Column('adminid', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.Column('token', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('adminid')
    )
    op.create_table('tagposts',
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.Column('tag_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.postid'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.tagid'], )
    )
    op.create_table('homecontents',
    sa.Column('homecontentid', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.VARCHAR(), nullable=False),
    sa.Column('theme', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('homecontentid')
    )
    op.create_table('projecttags',
    sa.Column('project_id', sa.INTEGER(), nullable=True),
    sa.Column('tag_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.projectid'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.tagid'], )
    )
    op.create_table('projects',
    sa.Column('projectid', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('shortdescription', sa.VARCHAR(), nullable=False),
    sa.Column('bigdescription', sa.VARCHAR(), nullable=True),
    sa.Column('link', sa.VARCHAR(), nullable=False),
    sa.Column('media', sa.VARCHAR(), nullable=True),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.Column('datecreated', sa.DATE(), nullable=True),
    sa.Column('englishtitle', sa.VARCHAR(), nullable=True),
    sa.Column('shortdescriptionenglish', sa.VARCHAR(), nullable=True),
    sa.Column('bigdescriptionenglish', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('projectid')
    )
    op.create_table('posts',
    sa.Column('postid', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('content', sa.VARCHAR(), nullable=False),
    sa.Column('media', sa.VARCHAR(), nullable=True),
    sa.Column('active', sa.BOOLEAN(), nullable=True),
    sa.Column('datecreated', sa.DATE(), nullable=True),
    sa.Column('englishtitle', sa.VARCHAR(), nullable=True),
    sa.Column('descriptionenglish', sa.VARCHAR(), nullable=True),
    sa.Column('contentenglish', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('postid')
    )
    # ### end Alembic commands ###
