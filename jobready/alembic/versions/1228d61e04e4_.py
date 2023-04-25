"""empty message

Revision ID: 1228d61e04e4
Revises: 252fd91ed428
Create Date: 2023-04-25 21:37:28.309430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1228d61e04e4'
down_revision = '252fd91ed428'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('templates')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'templates',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('preview', sa.VARCHAR(), nullable=True),
        sa.Column('template_name', sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###
