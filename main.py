
from fastapi import FastAPI
from router.actor import actor
from router.gender import gender
from router.director import director
from router.studio import studio
from router.collection import collection
from router.movie import movie

app = FastAPI()

app.include_router(actor, tags={"Actor"})
app.include_router(gender, tags={"Genero"})
app.include_router(director, tags={"Director"})
app.include_router(studio, tags={"Estudio"})
app.include_router(collection, tags={"Coleccion"})
app.include_router(movie, tags={"Pelicula"})

