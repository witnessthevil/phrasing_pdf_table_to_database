import pydeequ 
from pydeequ.analyzers import *
from pydeequ.checks import *
from pydeequ.verification import *
from Logger import Logger
from pyspark.sql import SparkSession
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
from sqlalchemy import text
from dotenv import dotenv_values
from pathlib import Path
import os
import boto3
import json

#sending quality metadata to dynamo db
logger = Logger().get_logger(__name__)
config = dotenv_values(os.path.join(Path(__file__).parent,"environment.env"))
endpoint=config["host"]
username=config["user"]
password=config["password"]
port=config["port"]
dbname=config["dbname"]
access_key=config["access_key"]
secret_key=config["secret_key"]
select_data="select * from world_data"

def spark_session():
    logger.info("starting spark session")
    spark = SparkSession.builder.master("local")\
        .config("spark.jars.packages", 'com.amazon.deequ:deequ:1.1.0_spark-3.0-scala-2.12')\
        .config("spark.jars.excludes", pydeequ.f2j_maven_coord).appName("realityisdead").getOrCreate()
    return spark

def connecting_to_redshift():
    engine_string = f"postgresql+psycopg2://{username}:{password}@{endpoint}:{port}/{dbname}"
    engine = create_engine(engine_string)
    df = pd.read_sql_query(select_data,engine)
    return df

def connecting_to_dynamo():
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="us-east-1"
    )
    table = session.resource("dynamodb").Table("employees")

    table.put_item(
        Item = {
            "name":"Danie2",
            "id":100
        }
    )

def data_quality_checking(session,df):
    check = Check(session,CheckLevel.Warning,"check mutiple things")

    result = VerificationSuite(session)\
                .onData(df)\
                .addCheck(check\
                .hasSize(lambda x: x >= 0))\
                .run()

    jsonic = VerificationResult.checkResultsAsJson(session,result)
    print(jsonic)

    

def main():
    session = spark_session()
    panda_df = connecting_to_redshift()
    df = session.createDataFrame(panda_df)
    data_quality_checking(session,df)
    

if __name__ == "__main__":
    main()


