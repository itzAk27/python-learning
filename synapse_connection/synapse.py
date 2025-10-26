import pandas as pd
import jaydebeapi
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

server = 'workspace-synapse-dw.sql.azuresynapse.net'
database = 'sqsynapsedw'
username = 'sa1'
password = 'Godrej@12345'
port = 1433

jdbc_url = f"jdbc:sqlserver://{server}:1433;" \
           f"database={database};" \
           "encrypt=true;" \
           "trustServerCertificate=false;" \
           "hostNameInCertificate=*.sql.azuresynapse.net;" \
           "loginTimeout=30;"

jdbc_driver_path = '/home/akhtar/Desktop/ODBC_TESTING/sqljdbc_12.10/enu/jars/mssql-jdbc-12.10.0.jre11.jar'
jdbc_driver_class = 'com.microsoft.sqlserver.jdbc.SQLServerDriver'


def get_synapse_connection(): 
    try: 
        conn = jaydebeapi.connect(
            jdbc_driver_class,
            jdbc_url,
            {'user': username, 'password': password},
            jars=jdbc_driver_path
        )

        return conn
    except Exception as e:
        print(e)
        return e 


def read_synapse_table(query):
    conn = get_synapse_connection()
    cursor = conn.cursor()
    cursor.execute(query)

    columns = [desc[0] for desc in cursor.description]  # get column names
    rows = cursor.fetchall()  # get all rows
    
    df = pd.DataFrame(rows, columns=columns)
    cursor.close()
    conn.close()

    print(df.head())
    return df


def exec_synapse_query(query):
    conn = get_synapse_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully ")
    except Exception as e:
        print(e)


def write_dataframe_table(data_frame, table_name, mode="append"):
    try:
        data_frame.write \
            .format("com.microsoft.sqlserver.jdbc.spark") \
            .option("url", jdbc_url) \
            .option("dbtable", f"dbo.{table_name}") \
            .option("user", username) \
            .option("password", password) \
            .mode("overwrite") \
            .save()
    except ValueError as error :
        print("Connector write failed", error)



