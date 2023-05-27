import configparser
import logging
from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union

from binance.spot import Spot
from pandas import DataFrame

from Exceptions.BinanceSpotPayException import BinanceSpotPayException
from Exchanges.Binance.BinanceInterface import BinanceInterface
from settings import basedir
from settings import setup_logger
from settings import singleton

# from typing import NoReturn

config = configparser.ConfigParser()
config.read(f"{basedir}/config.ini")

logger = logging.getLogger(__name__)
setup_logger(logger=logger)


@singleton
class BinanceSpotPay(BinanceInterface):
    def __init__(self, base_url: Optional[str] = "https://testnet.binance.vision"):
        # self.__apiKey = config["Binance"]["apiKey"]
        # self.__apiSecret = config["Binance"]["apiSecret"]
        self.__apiKey = config['Binance']['apiKey']
        self.__apiSecret = config['Binance']['apiSecret']
        self.__client = Spot(
            api_key=self.__apiKey, api_secret=self.__apiSecret, base_url=base_url
        )

    def pay_history(
            self,
            startTime: Optional[int] = None,
            endTime: Optional[int] = None,
            limit: Optional[int] = 100,
            recvWindow: Optional[int] = None,
    ):
        """
        limit (int, optional): default value is 100 and maximum value is 100
        recvWindow (int, optional): the value cannot be greater than 60000

        """
        try:
            if limit > 500:
                raise BinanceSpotPayException(err='limit over maximum value: 500')
            elif recvWindow > 60000:
                raise BinanceSpotPayException(err='recvWindow over limit 60000')

            output = self.__client.pay_history(
                startTime=startTime,
                endTime=endTime,
                limit=limit,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotPayException(err=Exception)

