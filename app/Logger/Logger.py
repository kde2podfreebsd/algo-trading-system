# import coloredlogs
import logging.config
import yaml

def setup_logger(logger):
    with open('../../logging.yaml', 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
        # coloredlogs.install()
        logging.config.dictConfig(config)
        # coloredlogs.install(level='DEBUG', logger=logger)