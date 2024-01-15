from fastapi import APIRouter, Response
from schema.movie_schema import MovieSchema
from config.db import conn
from model.movie_model import movieModel
from starlette.status import HTTP_204_NO_CONTENT


movie = APIRouter()

@movie.get("/movie")
def get_movies():
    return [x._asdict() for x in conn.execute(movieModel.select()).fetchall()]

@movie.post("/movie")
def create_movie(data_movie: MovieSchema):    
    new_movie = {
        "nombre": data_movie.nombre,
        "actor_id": data_movie.actor_id,
        "collection_id": data_movie.collection_id,
        "director_id": data_movie.director_id,
        "gender_id": data_movie.gender_id,
        "studio_id": data_movie.studio_id
    }

    # Obtener solo las columnas relevantes para la inserción
    relevant_columns = [column for column in movieModel.columns if column.key in new_movie]

    # Crear una nueva sentencia de inserción solo con las columnas relevantes
    stmt = movieModel.insert().values({column.key: new_movie[column.key] for column in relevant_columns})
    
    try:
        result = conn.execute(stmt)
        conn.commit()
        inserted_id = result.inserted_primary_key[0]
        
        # Devolvemos el nuevo elemento insertado
        return conn.execute(movieModel.select().where(movieModel.c.id == inserted_id)).first()._asdict()
 
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
        conn.rollback()
        return {"error": "Error al insertar en la base de datos"}
    
    #result = conn.execute(movieModel.insert().values(**new_movie))
    #conn.commit()
    #return conn.execute(movieModel.select().where(movieModel.c.id == result.lastrowid)).first()._asdict()