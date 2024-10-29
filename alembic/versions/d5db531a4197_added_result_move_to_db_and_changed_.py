"""Added result_move to DB and changed size of result_pos

Revision ID: d5db531a4197
Revises: 7480b43ff43a
Create Date: 2024-10-30 00:26:18.157578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5db531a4197'
down_revision: Union[str, None] = '7480b43ff43a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tests', sa.Column('result_move', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'tests', ['result_move'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tests', type_='unique')
    op.drop_column('tests', 'result_move')
    # ### end Alembic commands ###