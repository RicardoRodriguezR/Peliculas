from fastapi import APIRouter, Response
from schema.actor_schema import ActorSchema
from config.db import conn
from model.actor_model import actorModel
from starlette.status import HTTP_204_NO_CONTENT


actor = APIRouter()

@actor.get("/actor")
def get_actores():
    return [x._asdict() for x in conn.execute(actorModel.select()).fetchall()]

@actor.post("/actor")
def create_actor(data_actor: ActorSchema):
    new_actor = {"nombre": data_actor.nombre, 
                 "apellido": data_actor.apellido, 
                 "nombre_artistico": data_actor.nombre_artistico, 
                 "edad": data_actor.edad}
    result = conn.execute(actorModel.insert().values(new_actor))
    conn.commit()
    return conn.execute(actorModel.select().where(actorModel.c.id == result.lastrowid)).first()._asdict()

@actor.get("/actor/{id}")
def get_actor(id: str):
    result = conn.execute(actorModel.select().where(actorModel.c.id == id)).fetchone()    
    return result._asdict()


@actor.delete("/actor/{id}")
def delete_actor(id: str):
    result = conn.execute(actorModel.delete().where(actorModel.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@actor.put("/actor/{id}")
def upgrade_actor(id: str, upgrade_actor: ActorSchema):
    conn.execute(actorModel.update().values(nombre = upgrade_actor.nombre,
                                                apellido = upgrade_actor.apellido, 
                                                nombre_artistico = upgrade_actor.nombre_artistico, 
                                                edad = upgrade_actor.edad).where(actorModel.c.id == id))
    conn.commit()
    return conn.execute(actorModel.select().where(actorModel.c.id == id)).first()._asdict()