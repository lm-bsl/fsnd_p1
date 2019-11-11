"""empty message

Revision ID: ca9a2bd8a393
Revises: f33494c05d42
Create Date: 2019-11-11 22:31:30.445482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca9a2bd8a393'
down_revision = 'f33494c05d42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###