import logging

from binance.error import ClientError
from binance.error import ParameterArgumentError
from binance.error import ParameterRequiredError
from binance.error import ParameterTypeError
from binance.error import ParameterValueError
from binance.error import ServerError

from settings import setup_logger


class BinanceSpotPayException(Exception):
    def __init__(
        self,
        err: Exception
        | ClientError
        | ServerError
        | ParameterRequiredError
        | ParameterValueError
        | ParameterTypeError
        | ParameterArgumentError,
    ):
        self.logger = logging.getLogger(__name__)
        setup_logger(logger=self.logger)
        self.error = err
        logging.error(self.error)

    def __str__(self):
        return f"BinanceSDK.Binance.Spot.Pay.Exception: {self.error}"
