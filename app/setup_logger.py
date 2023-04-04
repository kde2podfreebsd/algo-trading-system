import coloredlogs
import logging.config
import yaml
import os

basedir = os.path.abspath(os.path.dirname(__file__))

def setup_logger(logger):
    with open(f'{basedir}/../logging.yaml', 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        coloredlogs.install()
        logging.config.dictConfig(config)
        coloredlogs.install(level='INFO', logger=logger)