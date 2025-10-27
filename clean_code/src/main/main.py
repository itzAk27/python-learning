import configparser
from databases.mysql_conn import * 
from databases.mysql_conn_class import *
from labors.labors_class import labors
from loguru import logger


config = configparser.ConfigParser()
config.read("resources/config.ini")


def main():
    mysql_db_conn = MySqlConnection(config)
    mysql_db_conn.mysql_db_connection()

    curd_operation = MySqlCRUDOperation(mysql_db_conn.connection)

    labor_obj = labors("Sharik", "Khan", "90000000", "mistry", curd_operation)
    # labor_obj.save_to_database(curd_operation)


if __name__ == "__main__":
    main()