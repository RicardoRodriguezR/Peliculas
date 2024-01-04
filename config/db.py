from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:Ricardo.911026@localhost:3306/peliculas")
conn = engine.connect()
meta_data = MetaData()