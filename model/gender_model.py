from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

genderModel = Table("gender", meta_data,
               Column("id", Integer, primary_key=True, autoincrement=True),
               Column("nombre", String(90), nullable=False))

meta_data.create_all(engine)