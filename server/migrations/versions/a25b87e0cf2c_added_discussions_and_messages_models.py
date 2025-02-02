"""Added discussions and messages models

Revision ID: a25b87e0cf2c
Revises: 3773b51188b1
Create Date: 2024-07-10 06:54:50.402929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a25b87e0cf2c'
down_revision = '3773b51188b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discussions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('book_club_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_club_id'], ['book_clubs.id'], name=op.f('fk_discussions_book_club_id_book_clubs')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('discussions')
    # ### end Alembic commands ###
