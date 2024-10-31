"""Added type_of_position to DB

Revision ID: 631c21b21a99
Revises: d5db531a4197
Create Date: 2024-10-31 23:28:28.661958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '631c21b21a99'
down_revision: Union[str, None] = 'd5db531a4197'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tests', sa.Column('type_of_position', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tests', 'type_of_position')
    # ### end Alembic commands ###
