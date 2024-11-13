from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f656e7ad8a8d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_products_id', table_name='products')
    op.drop_index('ix_products_name', table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('status', sa.VARCHAR(), nullable=True),
    sa.Column('stock_quantity', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_products_name', 'products', ['name'], unique=False)
    op.create_index('ix_products_id', 'products', ['id'], unique=False)
    # ### end Alembic commands ###
