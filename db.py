from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String,)

engine = create_engine('sqlite:///db.sqlite3', echo=True)
metadata = MetaData()
metadata.bind = engine

menus = Table(
    'menus', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True),
    Column('kcal', Integer),
    Column('image', String),
)
