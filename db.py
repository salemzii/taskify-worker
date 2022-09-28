from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
import os



db_uri = os.getenv("DATABASE_URL")
if db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://")

engine = create_engine(db_uri)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    appdb = SessionLocal()
    try:
        yield appdb
    finally:
        appdb.close()
        

def drop_table(table_name, engine=engine):
    Base = declarative_base()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[table_name]
    if table is not None:
        Base.metadata.drop_all(engine, [table], checkfirst=True)


import psycopg2
from psycopg2 import Error

def ConnectPostgres():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="yiutwxdz",
                                    password="2LuL55EjQeO_mzqIEGooGZ10GHvWQeL5",
                                    host="jelani.db.elephantsql.com",
                                    database="yiutwxdz")

        # Create a cursor to perform database operations
        cursor = connection.cursor()

        return cursor

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
