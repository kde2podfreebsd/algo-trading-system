from app.setup_logger import setup_logger
import logging


class TaLibBaseException(Exception):
    def __init__(self, err: Exception):
        self.logger = logging.getLogger(__name__)
        setup_logger(logger=self.logger)
        self.error = err
        logging.error(self.error)

    def __str__(self):
        return f"app.TaLib.TABase.Exception: {self.error}"