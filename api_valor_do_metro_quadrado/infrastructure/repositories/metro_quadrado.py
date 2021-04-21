from sqlalchemy import Table, Column, Integer, Float, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

from . import database


metadata = MetaData()

metro_quadrado_table = Table(
    'metro_quadrado',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('valor', Float),
    Column('data_de_cadastro', DateTime),
)


class MetroQuadradoRepository:

    _table = metro_quadrado_table

    @classmethod
    async def get(cls):
        statement = cls._table.select()
        result = await database.fetch_one(statement)

        return dict(result)
