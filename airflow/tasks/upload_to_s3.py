from Logger import Logger
import boto3
from dotenv import dotenv_values
import os
from multiprocessing import Pool
import time
import psutil

logger = Logger().get_logger(__name__)

file_1 = "/tmp/example1.csv"
file_2 = "/tmp/example2.csv"
config = dotenv_values(os.path.join(os.path.dirname(__file__),"environment.env"))
print(config)
s3_client = boto3.client(
            service_name='s3',
            region_name=config["region"],
            aws_access_key_id=config["access_key"],
            aws_secret_access_key=config["secret_key"]
        )
if __name__ == "__main__":
    logger.info("now performing the load part!")
    start_time = time.perf_counter()
    s3_client.upload_file(file_1,config["bucket_name"],"file1.csv")
    s3_client.upload_file(file_2,config["bucket_name"],"file_2.csv")
    end_time = time.perf_counter()
    logger.info(f'Extract CPU usage {psutil.cpu_percent()}%')
    logger.info(f"writing csv to s3 have used {end_time - start_time}s")