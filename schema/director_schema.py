from pydantic import BaseModel

class DirectorSchema(BaseModel):
    nombre:str
    apellido:str
    edad:str