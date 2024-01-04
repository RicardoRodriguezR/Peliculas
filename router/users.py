from fastapi import APIRouter
from schema.user_schema import UserSchema
from config.db import conn
from model.actor import actor


user = APIRouter()

@user.get("/")
def root():
    return {"Hola perrito"}

@user.post("/api/user")
def create_actor(data_actor: UserSchema):
    new_actor = data_actor.dict()
    conn.execute(actor.insert().values(new_actor))
    return "success"
    
@user.put("/api/user")
def update_user(data_user:UserSchema):
    pass