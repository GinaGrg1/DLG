import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def get_max_row(spark, infolder):
    df = spark.read.load(infolder)
    max_temp = df.agg({"ScreenTemperature":"max"}).collect()[0][0]
    max_temp_row = df.where(col("ScreenTemperature") == max_temp).collect()
    return max_temp_row


if __name__ == "__main__":
    spark = SparkSession.builder.master('local').appName('load weather parquet').getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    parser = argparse.ArgumentParser("Read parquet files and get Max temperature details")
    parser.add_argument('-i', '--infolder', type=str, 
                        help="Folder where all the weather files are stored as parquet", required=True)
    
    args = parser.parse_args()
    folder = args.infolder
    print("Hottest day details: \n")
    print(get_max_row(spark, folder))