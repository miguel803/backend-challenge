"""cria tabela metro_quadrado

Revision ID: 72481994c8b0
Revises: 
Create Date: 2021-04-19 07:42:13.916374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72481994c8b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'metro_quadrado',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('valor', sa.Float),
        sa.Column('data_de_cadastro', sa.DateTime),
    )


def downgrade():
    pass
