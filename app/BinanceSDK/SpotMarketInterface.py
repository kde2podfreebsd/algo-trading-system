from binance.spot import Spot
from pandas.core.frame import DataFrame
from typing import Optional, List, NoReturn, Union, Mapping, Text, Tuple, Sequence, Dict, Set
from abc import ABCMeta, abstractmethod, abstractstaticmethod, abstractproperty


class BinanceSpotMarketInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self) -> NoReturn:
        self.__client = Spot()

    @staticmethod
    @abstractstaticmethod
    def make_dataFrame(data: List[List[str]]) -> DataFrame:
        """
        Create DataFrame from data
        :param data:
        :return DataFrame(data):
        """
        return DataFrame(data)

    @abstractmethod
    def agg_trades(
            self,
            symbol: str,
            limit: Optional[int],
            formId: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int]
    ) \
            -> List[Dict[str: str]]:
        """
        Get aggregation trades info
        :param symbol:
        :param limit:
        :param formId:
        :param startTime:
        :param endTime:
        :return:
        """

    @abstractmethod
    def avg_price(self, symbol: str) -> Dict[str: Union[int | float]]:
        """
        Get average price of ticker for last 5 min
        :param symbol:
        :return:
        """

    @abstractmethod
    def book_ticker(self, symbol: str) -> Dict[str: str] | List[Dict[str: str]]:
        """
        Best price/qty on the order book for a symbol or symbols
        :param symbol:
        :return:
        """

    @abstractmethod
    def depth(self, symbol: str, limit: Optional[int]) -> Dict[str: Union[int | List[List[str]]]]:
        """
        Get orderbook
        :param symbol:
        :param limit:
        :return:
        """

    @abstractmethod
    def exchange_info(self, symbols: str | List[str]) -> Dict[str: Union[str | List[str] | List[List[str]] | List[Dict[str: str]]]]:
        """
        Current exchange trading rules and symbol information
        :param symbols:
        :return:
        """

    @abstractmethod
    def historical_trades(self):
        pass

    @abstractmethod
    def kLines(self, symbol: str, interval: str, limit: Optional[int]) -> List[List[str]]:
        """
        Kline/Candlestick Data
        :param symbol:
        :param interval:
        :param limit:
        :return:
        """

    @abstractmethod
    def ping(self) -> Set:
        """
        Test connectivity to the Rest API.
        :return:
        """

    @abstractmethod
    def rolling_window_ticker(self, symbol: str, windowSize: str, requestType: str) -> Dict[str: Union[str | int | float]]:
        """
        The window used to compute statistics is typically slightly wider than requested windowSize.
        :param symbol:
        :param windowSize:
        :param requestType [FULL | MINI]:
        :return:
        """

    @abstractmethod
    def ticker_24hr(self, symbols: List[str], requestType: str) -> List[Dict[str: Union[str | int | float]]]:
        """
        24hr Ticker Price Change Statistics
        :param symbols:
        :param requestType:
        :return:
        """

    @abstractmethod
    def ticker_price(self, symbols: List[str]) -> List[Dict[str: str]]:
        """
        Symbol Price Ticker
        :param symbols:
        :return:
        """

    @abstractmethod
    def time(self) -> Dict[str: int]:
        """
        Test connectivity to the Rest API and get the current server time.
        :return:
        """

    @abstractmethod
    def trades(self, symbol: str, limit: Optional[int]) -> List[Dict[str: Union[str | int | float | bool]]]:
        """
        Get recent trades (up to last 500).
        :param symbol:
        :param limit:
        :return:
        """

    @abstractmethod
    def uikLines(
            self,
            symbol: str,
            interval: str,
            limit: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int]
    ) -> List[List[str]]:
        """
        Kline/Candlestick Data
        :param symbol:
        :param interval:
        :param limit:
        :param startTime:
        :param endTime:
        :return:
        """

    @abstractmethod
    def spotTickers(self) -> List[str]:
        """
        Get available spot tickers
        :return:
        """

