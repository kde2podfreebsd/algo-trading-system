import configparser
import logging
from typing import Dict
from typing import Optional
from typing import Sequence
from typing import Union

from binance.spot import Spot

from Exceptions.BinanceSpotFiatException import BinanceSpotFiatException
from settings import basedir
from settings import setup_logger
from settings import singleton

# from datetime import datetime
# from typing import Any
# from typing import List
# from pandas import DataFrame

# from typing import NoReturn

config = configparser.ConfigParser()
config.read(f"{basedir}/config.ini")

logger = logging.getLogger(__name__)
setup_logger(logger=logger)


@singleton
class BinanceSpotFiat(object):
    __client: Spot

    def __init__(self, base_url: Optional[str] = "https://testnet.binance.vision"):
        # self.__apiKey = config["Binance"]["apiKey"]
        # self.__apiSecret = config["Binance"]["apiSecret"]
        self.__apiKey = config["Binance"]["apiKey"]
        self.__apiSecret = config["Binance"]["apiSecret"]
        self.__client = Spot(
            api_key=self.__apiKey, api_secret=self.__apiSecret, base_url=base_url
        )

    def fiat_order_history(
        self,
        transactionType: int,
        beginTime: Optional[int] = None,
        endTime: Optional[int] = None,
        page: Optional[int] = 1,
        rows: Optional[int] = 100,
        recvWindow: Optional[int] = 60000,
    ) -> Sequence[Dict[int, Union[str | int | float | bool]]]:
        try:
            output = self.__client.fiat_order_history(
                transactionType=transactionType,
                beginTime=beginTime,
                endTime=endTime,
                page=page,
                rows=rows,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotFiatException(err=Exception)
