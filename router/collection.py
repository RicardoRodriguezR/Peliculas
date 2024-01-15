from fastapi import APIRouter, Response
from schema.collection_schema import CollectionSchema
from config.db import conn
from model.collection_model import collectionModel
from starlette.status import HTTP_204_NO_CONTENT

collection = APIRouter()

@collection.get("/collection")
def get_collections():
    return [x._asdict() for x in conn.execute(collectionModel.select()).fetchall()]

@collection.post("/collection")
def create_collection(data_collection: CollectionSchema):
    new_collection = {"nombre": data_collection.nombre}
    result = conn.execute(collectionModel.insert().values(new_collection))
    conn.commit()
    return conn.execute(collectionModel.select().where(collectionModel.c.id == result.lastrowid)).first()._asdict()

@collection.get("/collection/{id}")
def get_collection(id: str):
    result = conn.execute(collectionModel.select().where(collectionModel.c.id == id)).fetchone()
    return result._asdict()

@collection.delete("/collection/{id}")
def delete_collection(id: str):
    conn.execute(collectionModel.delete().where(collectionModel.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@collection.put("/collection/{id}")
def upgrade_collection(id:str, upgrade_gender: CollectionSchema):
    conn.execute(collectionModel.update().values(nombre = upgrade_gender.nombre).where(collectionModel.c.id == id))
    conn.commit()
    return conn.execute(collectionModel.select().where(collectionModel.c.id == id)).first()._asdict()