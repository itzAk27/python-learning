import configparser
from databases.mysql_conn import * 
from databases.mysql_conn_class import *
from labors.labors_class import labors, Person, Mistry
from loguru import logger


config = configparser.ConfigParser()
config.read("resources/config.ini")

 
def main():
    mysql_db_conn = MySqlConnection(config)
    mysql_db_conn.mysql_db_connection()

    curd_operation = MySqlCRUDOperation(mysql_db_conn.connection)

    # labors.login_logout(config, curd_operation, None, "Akhtar", "Khan")

    obj = Mistry("Imran", "Pathan", "10000", "Admin", "A, B", curd_operation, config)
    obj.save_to_skill_table()


if __name__ == "__main__":
    main()