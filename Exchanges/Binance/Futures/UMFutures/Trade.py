import configparser
import logging

from binance.error import ClientError
from binance.lib.utils import config_logging
from binance.um_futures import UMFutures

from settings import basedir
from settings import setup_logger

# from datetime import datetime
# from datetime import timezone
# from typing import Any
# from typing import Dict
# from typing import List
# from typing import Optional
# from typing import Sequence
# from typing import Union
# from pandas import DataFrame
# from Exceptions import BinanceSpotMarketException
# from Exchanges.Binance.BinanceInterface import BinanceInterface


config = configparser.ConfigParser()
config.read(f"{basedir}/config.ini")

logger = logging.getLogger(__name__)
setup_logger(logger=logger)


class UMFuturesClient(object):
    __instance = None

    def __init__(self):
        if not UMFuturesClient.__instance:
            self.__apiKey = config["Binance_Futures"]["apiKey"]
            self.__apiSecret = config["Binance_Futures"]["apiSecret"]

            config_logging(logging, logging.DEBUG)

            self.um_futures_client = UMFutures(self.__apiKey, self.__apiSecret)
            self.um_futures_client.base_url = "https://testnet.binancefuture.com"
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        try:
            if not cls.__instance:
                cls.__instance = UMFuturesClient()
            return cls.__instance
        except Exception as e:
            return e

    def makeOrder(self, symbol: str, orderType: str, side: str, quantity: float):
        try:
            response = self.um_futures_client.new_order(
                symbol=symbol,
                side=side,
                type=orderType,
                quantity=quantity,
            )
            logging.info(response)
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getAccountTrades(self):
        try:
            response = self.um_futures_client.get_account_trades(
                symbol="BTCUSDT", recvWindow=6000
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )


if __name__ == "__main__":
    umf = UMFuturesClient()
    # t = umf.makeOrder(symbol="BTCUSDT",orderType='MARKET',side="BUY", quantity=0.01)
    # output = umf.getAccountTrades()
    # print(output)
