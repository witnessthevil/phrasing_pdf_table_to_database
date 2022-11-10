import psycopg2
from pathlib import Path
from Logger import Logger
from dotenv import dotenv_values
import os
from sqlalchemy import create_engine,text

logger = Logger().get_logger(__name__)
config = dotenv_values(os.path.join(os.path.dirname(__file__),"environment.env"))

def connection():
    conn = psycopg2.connect(
        dbname= config["dbname"],
        user= config["user"], 
        password= config["password"], 
        host = config["host"],
        port = config["port"]
    )
    return conn


if __name__ == "__main__":
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * from pg_user;")
    conn.commit()
    cursor.close()
    conn.close()
    