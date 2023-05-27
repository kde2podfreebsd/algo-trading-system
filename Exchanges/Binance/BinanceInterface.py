import datetime
from abc import ABCMeta
from abc import abstractmethod
from typing import Any
from typing import List
from typing import Optional
from typing import Union

from pandas import DataFrame

from Exchanges.ExchangesInterface import ExchangesInterface

# from abc import abstractclassmethod
# from abc import abstractstaticmethod
# import pandas as pd


class BinanceInterface(ExchangesInterface):
    __metaclass__ = ABCMeta

    @property
    def modules(self):
        return self.__function_groups.keys()

    @property
    def exchangeName(self):
        return self._exchangeName

    @exchangeName.setter
    def exchangeName(self, value):
        self._exchangeName = value

    def makeTimePeriodDataFrame(
        self,
        startTIme: Union[str | datetime.datetime] = None,
        endTime: Union[str | datetime.datetime] = None,
        bar_interval: Any = None,
        symbol: str = None,
    ) -> DataFrame:
        """ """
        return DataFrame

    @abstractmethod
    def __init__(self, apiKeys: Optional[List[str]]):

        self.exchangeName = "Binance"
        self.__apiKey = apiKeys[0]
        self.__apiSecret = apiKeys[1]

    __function_groups = {
        "Market": [
            "agg_trades",
            "avg_price",
            "book_ticker",
            "depth",
            "exchange_info",
            "kLines",
            "ping",
            "rolling_window_ticker",
            "ticker_24hr",
            "ticker_price",
            "time",
            "trades",
            "uikLines",
            "spotTickers",
            "makeKLinesDataFrame",
            "makeTimePeriodDataFrame",
        ],
        "Fiat": ["", ""],
    }
