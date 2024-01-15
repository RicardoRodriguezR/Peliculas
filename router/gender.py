from fastapi import APIRouter, Response
from schema.gender_schema import GenderSchema
from config.db import conn
from model.gender_model import genderModel
from starlette.status import HTTP_204_NO_CONTENT

gender = APIRouter()

@gender.get("/gender")
def get_generos():
    return [x._asdict() for x in conn.execute(genderModel.select()).fetchall()]

@gender.post("/gender")
def create_gender(data_gender: GenderSchema):
    new_gender = {"nombre": data_gender.nombre}
    print(new_gender)
    result = conn.execute(genderModel.insert().values(new_gender))
    conn.commit()
    print(result)
    return conn.execute(genderModel.select().where(genderModel.c.id == result.lastrowid)).first()._asdict()

@gender.get("/gender/{id}")
def get_genders(id: str):
    result = conn.execute(genderModel.select().where(genderModel.c.id == id)).fetchone()
    return result._asdict()

@gender.delete("/gender/{id}")
def delete_gender(id: str):
    conn.execute(genderModel.delete().where(genderModel.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@gender.put("/gender/{id}")
def upgrade_gender(id:str, upgrade_gender: GenderSchema):
    conn.execute(genderModel.update().values(nombre = upgrade_gender.nombre).where(genderModel.c.id == id))
    conn.commit()
    return conn.execute(genderModel.select().where(genderModel.c.id == id)).first()._asdict()
