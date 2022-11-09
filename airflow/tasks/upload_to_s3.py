from Logger import Logger
import boto3
from dotenv import dotenv_values
import os
from multiprocessing import Pool

logger = Logger(__name__)

file_1 = "/tmp/example1.csv"
file_2 = "/tmp/example2.csv"
config = dotenv_values(os.path.join(os.path.dirname(__file__),"environment.env"))
s3_client = boto3.client(
            service_name='s3',
            region_name=config["region"],
            aws_access_key_id=config["access_key"],
            aws_secret_access_key=config["secret_key"]
        )

s3_client.upload_file(file_1,config["bucket_name"],file_1)
s3_client.upload_file(file_2,config["bucket_name"],file_2)
