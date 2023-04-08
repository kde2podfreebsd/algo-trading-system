import configparser
import logging.config
import os

import coloredlogs
import yaml
from envparse import Env

basedir = os.path.abspath(os.path.dirname(__file__))
env = Env()
config = configparser.ConfigParser()
config.read(f"{basedir}/../config.ini")

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default=f"postgresql+asyncpg://{config['POSTGRESQL']['user']}:{config['POSTGRESQL']['password']}@{config['POSTGRESQL']['host']}:{config['POSTGRESQL']['port']}/{config['POSTGRESQL']['database']}",
)

TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default=f"postgresql+asyncpg://{config['POSTGRESQL_TestDB']['user']}:{config['POSTGRESQL_TestDB']['password']}@{config['POSTGRESQL_TestDB']['host']}:{config['POSTGRESQL_TestDB']['port']}/{config['POSTGRESQL_TestDB']['database']}",
)


def setup_logger(logger):
    with open(f"{basedir}/../logging.yaml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        coloredlogs.install()
        logging.config.dictConfig(config)
        coloredlogs.install(level="INFO", logger=logger)
