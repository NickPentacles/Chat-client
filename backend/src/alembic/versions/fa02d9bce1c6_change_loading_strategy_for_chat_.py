"""Change loading strategy for chat.messages

Revision ID: fa02d9bce1c6
Revises: 1e2c291059be
Create Date: 2024-10-18 02:08:36.192000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa02d9bce1c6'
down_revision: Union[str, None] = '1e2c291059be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'chat', ['uuid'])
    op.create_unique_constraint(None, 'file', ['uuid'])
    op.create_unique_constraint(None, 'message', ['uuid'])
    op.create_unique_constraint(None, 'project', ['uuid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'project', type_='unique')
    op.drop_constraint(None, 'message', type_='unique')
    op.drop_constraint(None, 'file', type_='unique')
    op.drop_constraint(None, 'chat', type_='unique')
    # ### end Alembic commands ###