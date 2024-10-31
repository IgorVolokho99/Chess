"""Corrected name of column in DB

Revision ID: 140d0e534370
Revises: 631c21b21a99
Create Date: 2024-10-31 23:35:49.960394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '140d0e534370'
down_revision: Union[str, None] = '631c21b21a99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tests', sa.Column('result_moves', sa.String(), nullable=False))
    op.drop_constraint('tests_result_move_key', 'tests', type_='unique')
    op.create_unique_constraint(None, 'tests', ['result_moves'])
    op.drop_column('tests', 'result_move')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tests', sa.Column('result_move', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'tests', type_='unique')
    op.create_unique_constraint('tests_result_move_key', 'tests', ['result_move'])
    op.drop_column('tests', 'result_moves')
    # ### end Alembic commands ###
