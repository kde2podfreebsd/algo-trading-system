import configparser
import logging
import os
from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union

from binance.spot import Spot
from pandas import DataFrame

from Exceptions import BinanceSpotMarketException
from settings import basedir
from singletonWrapper import singleton

# from typing import NoReturn
# from settings import setup_logger

config = configparser.ConfigParser()
config.read(f"{basedir}/config.ini")


basedir = os.path.abspath(os.path.dirname(__file__))

# logger = logging.getLogger(__name__)
# setup_logger(logger=logger)


@singleton
class BinanceSpotMarket(object):
    def __init__(self, base_url: Optional[str] = "https://testnet.binance.vision"):
        # self.__apiKey = config["Binance"]["apiKey"]
        # self.__apiSecret = config["Binance"]["apiSecret"]
        self.__apiKey = (
            "ADRb78f3mJvYZ8lTO7JWXxKTu1rKKJK33W8wil1MUQ8MJmeC5wDFPRwwhai0x6db"
        )
        self.__apiSecret = (
            "4uA4YYCcYGeM1dBALkNhTsx29nG2gVOoZM5CmiusheGMquPL5NlnMl0c2Do3UTPv"
        )
        self.__client = Spot(
            api_key=self.__apiKey, api_secret=self.__apiSecret, base_url=base_url
        )

    def agg_trades(
        self,
        symbol: str,
        limit: Optional[int] = 10,
        formId: Optional[int] = None,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> Sequence[Dict[str, Union[str | int | float | bool]]]:
        try:
            output = self.__client.agg_trades(
                symbol=symbol,
                limit=limit,
                fromId=formId,
                startTime=startTime,
                endTime=endTime,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def avg_price(self, symbol: str) -> Dict[str, Union[int | str]]:
        try:
            output = self.__client.avg_price(symbol=symbol)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def book_ticker(self, symbols: List[str]) -> Sequence[Dict[str, str]]:
        try:
            output = self.__client.book_ticker(symbols=symbols)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def depth(
        self, symbol: str, limit: Optional[int] = None
    ) -> Dict[str, Union[Sequence[List[str]] | int]]:
        try:
            output = self.__client.depth(symbol=symbol, limit=limit)
            logging.debug(output)
            return output
        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def exchange_info(self, symbols: List[str]) -> Dict[str, Union[Any]]:
        try:
            output = self.__client.exchange_info(symbols=symbols)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def kLines(
        self,
        symbol: str,
        interval: str,
        limit: Optional[int] = 10,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> Sequence[List["str"]]:
        try:
            output = self.__client.klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=startTime,
                endTime=endTime,
            )
            # logging.debug(output)
            return output

        except Exception:
            #           raise BinanceSpotMarketException(err=Exception)
            pass

    def ping(self) -> Dict:
        try:
            output = self.__client.ping()
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def rolling_window_ticker(
        self, symbol: str, windowSize: str = "1d", requestType: str = "FULL"
    ) -> Dict[str, Union[str | int | float]]:
        try:
            output = self.__client.rolling_window_ticker(
                symbol=symbol, windowSize=windowSize, type=requestType
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def ticker_24hr(
        self, symbols: List[str], requestType: str = "FULL"
    ) -> Sequence[Dict[str, Union[str | int | float]]]:
        try:
            output = self.__client.ticker_24hr(symbols=symbols, type=requestType)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def ticker_price(self, symbols: List[str]) -> Sequence[Dict[str, str]]:
        try:
            output = self.__client.ticker_price(symbols=symbols)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def time(self) -> Dict[str, int]:
        try:
            output = self.__client.time()
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def trades(
        self, symbol: str, limit: Optional[int] = 10
    ) -> Dict[str, Union[str | int | float | bool]]:
        try:
            output = self.__client.trades(symbol=symbol, limit=limit)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def uikLines(
        self,
        symbol: str,
        interval: str = "1h",
        limit: Optional[int] = 10,
        startTime: Optional[int] = 1400000000000,
        endTime: Optional[int] = None,
    ) -> Sequence[List[str]]:
        try:
            endTime = endTime if endTime is not None else self.time().get("serverTime")
            output = self.__client.ui_klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=startTime,
                endTime=endTime,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def spotTickers(self) -> List[str]:
        try:
            output = list(map(lambda x: x.get("symbol"), self.__client.ticker_price()))
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    @staticmethod
    def make_dataFrame(data):
        return DataFrame(data)

    def makeKLinesDataFrame(
        self,
        symbol: str,
        bar_interval,
        startTime: datetime,
        endTime: Optional[datetime],
    ) -> DataFrame:
        try:
            print(startTime)

            data = self.kLines(
                symbol=symbol,
                interval=bar_interval,
                limit=1000,
                startTime=startTime,
                endTime=endTime,
            )

            df = self.make_dataFrame(data)

            df.columns = [
                "Open time",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                "Kline Close time",
                "Quote asset volume",
                "Number of trades",
                "Taker buy base asset volume",
                "Taker buy quote asset volume",
                "Ignore",
            ]
            for i in list(df["Open time"]):
                df = df.replace(i, datetime.fromtimestamp(i / 1000))

            return df

        except Exception:
            #           raise BinanceSpotMarketException(err=Exception)
            pass

    # def appendDataFrame(self, df1: DataFrame, ticker):
    #     df2 = self.makeKLinesDataFrame(
    #         symbol=ticker,
    #         bar_interval="1h",
    #         startTime=datetime(2022, 1, 1),
    #         endTime=datetime(2023, 3, 1),
    #     )
    #     # df1.loc[len(df2)] = list
    #     return df1


if __name__ == "__main__":
    b = BinanceSpotMarket()
    print(datetime.fromtimestamp(1643341200000 / 1000))
    df = b.makeKLinesDataFrame(
        symbol="BTCUSDT",
        bar_interval="1m",
        startTime=None,
        endTime=None,
    )

    print(df)

    # b.appendDataFrame(df1=df, ticker='BTCUSDT')
    # print(b.agg_trades(symbol='ETHBUSD'))
    # print(b.avg_price(symbol='ETHBUSD'))
    # print(b.book_ticker(symbols=['ETHBUSD']))
    # print(b.depth(symbol='ETHBUSD', limit=10))
    # print(b.exchange_info(symbols=['ETHBUSD']))
    # print(b.kLines(symbol='ETHBUSD', interval='1h'))
    # print(b.ping())
    # print(b.rolling_window_ticker(symbol='ETHBUSD'))
    # print(b.ticker_24hr(symbols=['ETHBUSD']))
    # print(b.ticker_price(symbols=['ETHBUSD']))
    # print(b.time())
    # print(b.trades(symbol='ETHBUSD'))
    # print(b.uikLines(symbol='ETHBUSD', interval='1h'))
    # print(b.spotTickers())
    # print(b.historical_trades())

    # print(b.makeKLinesDataFrame(symbol='BTCUSDT', bar_interval='1d', startTime=datetime(2023,4,3), endTime=None))
