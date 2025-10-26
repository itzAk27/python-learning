import configparser
from databases.mysql_conn import * 
from databases.mysql_conn_class import *
from loguru import logger


config = configparser.ConfigParser()
config.read("resources/config.ini")


def main():
    # Using Functional Approach
    # q = "select * from information_schema.TABLES limit 5;"
    # read_from_mysql(config, q)
    # logger.info("Program Completed")

    # Using Class Approach
    mysql_db_conn = MySqlConnection(config)
    curd_operation = MySqlCRUDOperation(mysql_db_conn.mysql_db_connection())
    # ret = curd_operation.read_from_mysql("select * from info")
    curd_operation.insert_into_mysql("Truncate table info")
    # logger.info(f"{ret}")
    mysql_db_conn.closer()


if __name__ == "__main__":
    main()