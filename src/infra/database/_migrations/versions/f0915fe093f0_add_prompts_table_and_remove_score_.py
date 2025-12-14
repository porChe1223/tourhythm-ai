"""Add prompts table and remove score_reason

Revision ID: f0915fe093f0
Revises: 160260937e80
Create Date: 2025-12-14 09:44:04.393186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0915fe093f0'
down_revision: Union[str, Sequence[str], None] = '160260937e80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
