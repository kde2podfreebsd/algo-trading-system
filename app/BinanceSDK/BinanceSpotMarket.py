import os
import configparser
import logging
from typing import Optional, NoReturn, List, Dict, Union, Any, Sequence
from binance.spot import Spot
from app.singletonWrapper import singleton
from app.Logger import setup_logger
from app.Exceptions import BinanceSpotMarketException
from datetime import datetime
from pandas import DataFrame

basedir = os.path.abspath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(f"{basedir}/../../config.ini")

logger = logging.getLogger(__name__)
setup_logger(logger=logger)


@singleton
class BinanceSpotMarket(object):
    def __init__(self, base_url: Optional[str] = "https://testnet.binance.vision") -> NoReturn:
        self.__apiKey = config['Binance']['apiKey']
        self.__apiSecret = config['Binance']['apiSecret']
        self.__client = Spot(api_key=self.__apiKey, api_secret=self.__apiSecret, base_url=base_url)

    def agg_trades(
            self,
            symbol: str,
            limit: Optional[int] = 10,
            formId: Optional[int] = None,
            startTime: Optional[int] = None,
            endTime: Optional[int] = None
    ) \
            -> Sequence[Dict[str, Union[str | int | float | bool]]]:
        try:
            output = self.__client.agg_trades(symbol=symbol, limit=limit, fromId=formId, startTime=startTime, endTime=endTime)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def avg_price(self, symbol: str) -> Dict[str, Union[int | str]]:
        try:
            output = self.__client.avg_price(symbol=symbol)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def book_ticker(self, symbols: List[str]) -> Sequence[Dict[str, str]]:
        try:
            output = self.__client.book_ticker(symbols=symbols)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def depth(self, symbol: str, limit: Optional[int] = None) -> Dict[str, Union[Sequence[List[str]] | int]]:
        try:
            output = self.__client.depth(symbol=symbol, limit=limit)
            logging.info(output)
            return output
        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def exchange_info(self, symbols: List[str]) -> Dict[str, Union[Any]]:
        try:
            output = self.__client.exchange_info(symbols=symbols)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def historical_trades(self):
        print(self.__client.historical_trades("BTCUSDT"))

    def kLines(
            self,
            symbol: str,
            interval: str,
            limit: Optional[int] = 10,
            startTime: Optional[int] = None,
            endTime: Optional[int] = None
    ) \
            -> Sequence[List['str']]:
        try:
            output = self.__client.klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=startTime,
                endTime=endTime
            )
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def ping(self) -> Dict:
        try:
            output = self.__client.ping()
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def rolling_window_ticker(self, symbol: str, windowSize: str = "1d", requestType: str = "FULL") -> Dict[str, Union[str | int | float]]:
        try:
            output = self.__client.rolling_window_ticker(symbol=symbol, windowSize=windowSize, type=requestType)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def ticker_24hr(self, symbols: List[str], requestType: str = "FULL") -> Sequence[Dict[str, Union[str | int | float]]]:
        try:
            output = self.__client.ticker_24hr(symbols=symbols, type=requestType)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def ticker_price(self, symbols: List[str]) -> Sequence[Dict[str, str]]:
        try:
            output = self.__client.ticker_price(symbols=symbols)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def time(self) -> Dict[str, int]:
        try:
            output = self.__client.time()
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def trades(self, symbol: str, limit: Optional[int] = 10) -> Dict[str, Union[str | int | float |bool]]:
        try:
            output = self.__client.trades(symbol=symbol, limit=limit)
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def uikLines(
            self,
            symbol: str,
            interval: str = "1h",
            limit: Optional[int] = 10,
            startTime: Optional[int] = 1400000000000,
            endTime: Optional[int] = 1500000000000
    ) -> Sequence[List[str]]:
        try:
            output = self.__client.ui_klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=startTime,
                endTime=endTime
            )
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    def spotTickers(self) -> List[str]:
        try:
            output = list(map(lambda x: x.get('symbol'), self.__client.ticker_price()))
            logging.info(output)
            return output

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

    @staticmethod
    def make_dataFrame(data):
        return DataFrame(data)

    def makeKLinesDataFrame(self, symbol: str, bar_interval, startTime: datetime, endTime: Optional[datetime]):
        try:
            if endTime is None:
                endTime = int(self.time().get('serverTime'))
            else:
                endTime = int(endTime.timestamp())

            if startTime is not None:
                startTime = int(startTime.timestamp())

            data = self.kLines(symbol=symbol, interval=bar_interval, limit=10000, startTime=startTime, endTime=endTime)
            df = self.make_dataFrame(data)
            df.columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Kline Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
            for i in list(df['Open time']):
                df = df.replace(i, datetime.fromtimestamp(i/1000))

            return df

        except Exception:
            raise BinanceSpotMarketException(err=Exception)

if __name__ == "__main__":
    b = BinanceSpotMarket()
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