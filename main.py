from schema.user_schema import UserSchema
from fastapi import FastAPI
from router.users import user

app = FastAPI()

app.include_router(user)
