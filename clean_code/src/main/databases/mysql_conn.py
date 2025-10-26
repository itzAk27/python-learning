import mysql.connector
from loguru import logger


def get_conn(config):
    try:
        mydb = mysql.connector.connect(
            host = config["mysql_database"]["host"],  
            user = config["mysql_database"]["user"],
            password = config["mysql_database"]["password"],
            database= config["mysql_database"]["database"] 
        )
        logger.info("Connection established successfully!")
        return mydb
    except mysql.connector.Error as err:
        logger.info(f"Error connecting to MySQL: {err}")
        raise err


def read_from_mysql(config, query):
    try:
        conn = get_conn(config)
        
        cursor = conn.cursor()
        cursor.execute(query)
        
        rows = cursor.fetchall()
        # for i in rows:
        #     logger.info(i)
        logger.info(rows)
        return rows
    except Exception as e:
        raise e
    finally:
        # print(cursor.close())        
        # print(conn.close())
        cursor.close()
        conn.close()


