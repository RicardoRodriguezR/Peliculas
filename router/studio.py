from fastapi import APIRouter, Response
from schema.studio_schema import StudioSchema
from config.db import conn
from model.studio_model import studioModel
from starlette.status import HTTP_204_NO_CONTENT

studio = APIRouter()

@studio.get("/studio")
def get_studios():
    return [x._asdict() for x in conn.execute(studioModel.select()).fetchall()]

@studio.post("/studio")
def create_studio(data_studio: StudioSchema):
    new_studio = {"nombre": data_studio.nombre}
    result = conn.execute(studioModel.insert().values(new_studio))
    conn.commit()
    return conn.execute(studioModel.select().where(studioModel.c.id == result.lastrowid)).first()._asdict()

@studio.get("/genstudioder/{id}")
def get_studio(id: str):
    result = conn.execute(studioModel.select().where(studioModel.c.id == id)).fetchone()
    return result._asdict()

@studio.delete("/studio/{id}")
def delete_studio(id: str):
    conn.execute(studioModel.delete().where(studioModel.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@studio.put("/studio/{id}")
def upgrade_studio(id:str, upgrade_gender: StudioSchema):
    conn.execute(studioModel.update().values(nombre = upgrade_gender.nombre).where(studioModel.c.id == id))
    conn.commit()
    return conn.execute(studioModel.select().where(studioModel.c.id == id)).first()._asdict()