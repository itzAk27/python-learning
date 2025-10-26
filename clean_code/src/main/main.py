import configparser
from databases.mysql_conn import * 
from loguru import logger


config = configparser.ConfigParser()
config.read("resources/config.ini")


def main():
    q = "select * from information_schema.TABLES limit 5;"
    read_from_mysql(config, q)
    logger.info("Program Completed")


if __name__ == "__main__":
    main()