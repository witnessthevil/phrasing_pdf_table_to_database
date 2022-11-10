import pydeequ 
from pydeequ.analyzers import *
from pydeequ.checks import *
from pydeequ.verification import *
from Logger import Logger
from pyspark.sql import SparkSession

#sending quality metadata to dynamo db
logger = Logger().get_logger(__name__)

def checking_data_quality(file):
    spark = SparkSession.builder.master("local").appName("realityisdead").getOrCreate()
    #check = Check(spark,CheckLevel.Error,"checking the data")
    df = spark.read.format("csv").option("header","false").option("inferSchema","true").load(file)
    df.printSchema()
    df.show()
    #result = VerificationSuite(spark).onData(df).addCheck()

if __name__ == "__main__":
    checking_data_quality("/Users/danie/new_thing/example1.csv")

