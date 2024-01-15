from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

movieModel = Table("movie", meta_data,
             Column("id", Integer, primary_key=True, autoincrement=True),
             Column("nombre", String(90), nullable=False),
             Column("actor_id", Integer, ForeignKey('actor.id'), nullable=False),
             Column("collection_id", Integer, ForeignKey('collection.id'), nullable=False),
             Column("director_id", Integer, ForeignKey('director.id'), nullable=False),
             Column("gender_id", Integer, ForeignKey('gender.id'), nullable=False),
             Column("studio_id", Integer, ForeignKey('studio.id'), nullable=False))


meta_data.create_all(engine)