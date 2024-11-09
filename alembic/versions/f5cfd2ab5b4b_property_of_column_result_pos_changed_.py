"""Property of column result_pos changed. Was unique=True, now unique=False

Revision ID: f5cfd2ab5b4b
Revises: 140d0e534370
Create Date: 2024-11-04 15:57:05.963133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5cfd2ab5b4b'
down_revision: Union[str, None] = '140d0e534370'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tests_result_pos_key', 'tests', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('tests_result_pos_key', 'tests', ['result_pos'])
    # ### end Alembic commands ###
