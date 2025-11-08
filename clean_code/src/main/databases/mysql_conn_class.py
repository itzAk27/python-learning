import mysql.connector
from loguru import logger


class MySqlConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None


    def mysql_db_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.config["mysql_database"]["host"],  
                user = self.config["mysql_database"]["user"],
                password = self.config["mysql_database"]["password"],
                database= self.config["mysql_database"]["database"] 
            )
            logger.info("Connection established successfully!")
            return self.connection
        except mysql.connector.Error as err:
            logger.error(f"Error connecting to MySQL: {err}")
            raise err


    def closer(self):
        if self.connection.is_connected():
            self.connection.close()
            logger.info("Connection Closed")


class MySqlCRUDOperation:
    def __init__(self, mysql_connection):
        self.connection = mysql_connection


    def read_from_mysql(self, query, params):
        try:
            logger.info(query)
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            logger.error(f"Error in query: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()
                logger.info("Cursor Closed")


    # Use Update, Insert and Delete Queries 
    def insert_into_mysql(self, query, params):
        try:
            logger.info(query)
            cursor = self.connection.cursor()
            cursor.execute(query, params)
        except Exception as e:
            logger.error(f"Error in query: {e}")
            raise e
        finally:
            if cursor:
                self.connection.commit()
                logger.info(f"Changes Commited")
                cursor.close()
                logger.info("Cursor Closed")


