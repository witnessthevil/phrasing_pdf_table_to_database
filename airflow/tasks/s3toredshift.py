import psycopg2
from pathlib import Path
from Logger import Logger
from dotenv import dotenv_values
import os
from sqlalchemy import create_engine,text
import time
import psutil

logger = Logger().get_logger(__name__)

config = dotenv_values(os.path.join(os.path.dirname(__file__),"environment.env"))

script_path = os.path.join(Path(__file__).parent,"sql")

create_table_sql = open(f"{script_path}/createtable.sql","r").read()

load_data_sql = open(f"{script_path}/loadcsvtoworlddata.sql","r")\
        .read().format( 
        bucket_name=config["bucket_name"],
        file_name="file_reset3.csv",
        access_key=config["access_key"],
        secret_key=config["secret_key"]
)



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
    logger.info("now load csv from s3 to redshift")
    start_time = time.perf_counter()

    conn = connection()
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    cursor.execute(load_data_sql)
    conn.commit()
    cursor.close()
    conn.close()

    end_time = time.perf_counter()
    logger.info(f'Extract CPU usage {psutil.cpu_percent()}%')
    logger.info(f"writing csv from s3 to redshift have used {end_time - start_time}s")