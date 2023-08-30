"""second commit

Revision ID: 3c900b6dc919
Revises: daf153523d16
Create Date: 2023-08-29 19:58:08.198217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c900b6dc919'
down_revision: Union[str, None] = 'daf153523d16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
