"""New Column phone_number

Revision ID: 6331c843b252
Revises: 
Create Date: 2025-08-27 11:58:50.427136

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6331c843b252'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Agregar la columna phone_number a la tabla users."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    """Eliminar la columna phone_number de la tabla users."""
    op.drop_column('users', 'phone_number')
