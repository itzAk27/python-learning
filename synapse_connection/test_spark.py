import synapse
from pyspark.sql import SparkSession
import numpy as np
from datetime import datetime, timedelta

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Spark DataFrame Example") \
    .config(
        "spark.jars", 
        "/home/akhtar/Desktop/synapse_connection/drivers/apache-spark-sql-connector.jar,"
        "/home/akhtar/Desktop/ODBC_TESTING/sqljdbc_12.10/enu/jars/mssql-jdbc-12.10.0.jre11.jar") \
    .getOrCreate()


# Generate data
np.random.seed(42)
ids = [int(x) for x in np.arange(1, 1001)]
names = [f'Name_{i}' for i in ids]
ages = [int(x) for x in np.random.randint(20, 60, size=1000)]
salaries = [int(x) for x in np.random.randint(30000, 150000, size=1000)]
departments = np.random.choice(['HR', 'Finance', 'IT', 'Marketing', 'Operations'], size=1000).tolist()
joindates = [
    datetime(2015, 1, 1) + timedelta(days=int(x))
    for x in np.random.randint(0, 365 * 10, size=1000)
]

# Combine data into list of tuples (rows)
data = list(zip(ids, names, ages, salaries, departments, joindates))

columns = ["ID", "Name", "Age", "Salary", "Department", "JoinDate"]
sdf = spark.createDataFrame(data, schema=columns)

# sdf.printSchema()
# exit(0)

# Use custom write function
synapse.write_dataframe_table(sdf, 'test_ak_tbl', "overwrite")

print("Task Completed")
