from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    #id: Optional[str]
    nombre: str
    apellido: str
    nombre_artistico: str
    edad: str