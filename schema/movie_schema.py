from pydantic import BaseModel

class MovieSchema(BaseModel):
    nombre: str
    actor_id: int
    collection_id: int
    director_id: int
    gender_id: int
    studio_id: int