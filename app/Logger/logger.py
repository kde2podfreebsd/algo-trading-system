import logging.config
import yaml
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Logger(object):
    logger = None

    def __init__(self) -> 'Configure Logger for application | Load config.yaml & wirte logs in file logs.log':
        with open(f'{basedir}/../../logger_config.yaml', 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        self.logger = logging.getLogger(__name__)

        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(f'{basedir}/logs/logs.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)

        self.logger.addHandler(file_handler)