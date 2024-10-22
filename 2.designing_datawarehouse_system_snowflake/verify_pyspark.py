from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Verify PySpark Installation") \
    .getOrCreate()

# Print Spark session information
print(spark)

# Stop Spark session
spark.stop()
