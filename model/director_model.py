from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

director_model = Table("director", meta_data,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("nombre", String(90), nullable=False),
                Column("apellido", String(90), nullable=False),
                Column("edad", String(90), nullable=False)) 

meta_data.create_all(engine)