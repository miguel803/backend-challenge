"""adiciona migração de dados da tabela metro_quadrado

Revision ID: 70a9e8597786
Revises: 72481994c8b0
Create Date: 2021-04-19 20:39:24.059426

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = '70a9e8597786'
down_revision = '72481994c8b0'
branch_labels = None
depends_on = None


def upgrade():
    from datetime import datetime

    stmt = text("insert into metro_quadrado (id, valor, data_de_cadastro) values (:id, :valor, :data_de_cadastro)")
    stmt = stmt.bindparams(id='1', valor=100.0, data_de_cadastro=datetime.now())
    op.execute(stmt)


def downgrade():
    pass
