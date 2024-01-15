from fastapi import APIRouter, Response
from schema.director_schema import DirectorSchema
from config.db import conn
from model.director_model import director_model
from starlette.status import HTTP_204_NO_CONTENT


director = APIRouter()

@director.get("/director")
def get_directores():
    return [x._asdict() for x in conn.execute(director_model.select()).fetchall()]

@director.post("/director")
def create_director(data_director: DirectorSchema):
    new_director = {"nombre": data_director.nombre, 
                 "apellido": data_director.apellido,  
                 "edad": data_director.edad}
    result = conn.execute(director_model.insert().values(new_director))
    conn.commit()
    return conn.execute(director_model.select().where(director_model.c.id == result.lastrowid)).first()._asdict()

@director.get("/director/{id}")
def get_director(id: str):
    result = conn.execute(director_model.select().where(director_model.c.id == id)).fetchone()    
    return result._asdict()


@director.delete("/director/{id}")
def delete_director(id: str):
    result = conn.execute(director_model.delete().where(director_model.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@director.put("/director/{id}")
def upgrade_director(id: str, upgrade_actor: DirectorSchema):
    conn.execute(director_model.update().values(nombre = upgrade_actor.nombre,
                                                apellido = upgrade_actor.apellido,  
                                                edad = upgrade_actor.edad).where(director_model.c.id == id))
    conn.commit()
    return conn.execute(director_model.select().where(director_model.c.id == id)).first()._asdict()