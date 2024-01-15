from pydantic import BaseModel

class ActorSchema(BaseModel):
    nombre: str
    apellido: str
    nombre_artistico: str
    edad: str