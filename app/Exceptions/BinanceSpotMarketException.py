from binance.error import ClientError, ServerError, ParameterRequiredError, \
ParameterValueError, ParameterTypeError, ParameterArgumentError
from app.Logger import setup_logger
import logging

class BinanceSpotMarketException(Exception):
    def __init__(self, err: Exception | ClientError | ServerError | ParameterRequiredError | ParameterValueError | ParameterTypeError | ParameterArgumentError):
        self.logger = logging.getLogger(__name__)
        setup_logger(logger=self.logger)
        self.error = err
        logging.error(self.error)

    def __str__(self):
        return f"Binance.Spot.Market Exception: {self.error}"