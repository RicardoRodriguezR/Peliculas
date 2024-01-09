from fastapi import APIRouter, Response
from schema.user_schema import UserSchema
from config.db import conn
from model.actor import actor
from starlette.status import HTTP_204_NO_CONTENT


user = APIRouter()

@user.get("/users")
def get_users():
    return [x._asdict() for x in conn.execute(actor.select()).fetchall()]

@user.post("/user")
def create_actor(data_actor: UserSchema):
    new_actor = {"nombre": data_actor.nombre, 
                 "apellido": data_actor.apellido, 
                 "nombre_artistico": data_actor.nombre_artistico, 
                 "edad": data_actor.edad}
    result = conn.execute(actor.insert().values(new_actor))
    conn.commit()
    return conn.execute(actor.select().where(actor.c.id == result.lastrowid)).first()._asdict()

@user.get("/user/{id}")
def get_user(id: str):
    result = conn.execute(actor.select().where(actor.c.id == id)).fetchone()    
    return result._asdict()


@user.delete("/user/{id}")
def delete_user(id: str):
    result = conn.execute(actor.delete().where(actor.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/user/{id}")
def upgrade_user(id: str, update_actor: UserSchema):
    result = conn.execute(actor.update().values(nombre = update_actor.nombre,
                                                apellido = update_actor.apellido, 
                                                nombre_artistico = update_actor.nombre_artistico, 
                                                edad = update_actor.edad).where(actor.c.id == id))
    return "Update"