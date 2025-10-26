import configparser
from loguru import logger 


config = configparser.ConfigParser()

config.read("config.ini")

name = config["basic_info"]["name"]

logger.info(name)