import pandas as pd
from app.singletonWrapper import singleton
from typing import Optional, List, NoReturn, Union, Mapping, Text, Tuple, Sequence
from binance.spot import Spot
# from binance.error import ClientError, ServerError, ParameterRequiredError, \
#     ParameterValueError, ParameterTypeError, ParameterArgumentError
# from requests.exceptions import ConnectionError


@singleton
class BinanceSpot():
    def __init__(self) -> NoReturn:
        self.__client = Spot()
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)

    def agg_trades(self):
        # print(self.__client.agg_trades("BTCUSDT"))
        print(self.__client.agg_trades(symbol="BTCUSDT", limit=10, fromId=2231, startTime = 10, endTime=20))

    def avg_price(self):
        print(self.__client.avg_price(symbol="BTCUSDT"))

    def book_ticker(self):
        print(self.__client.book_ticker(symbol="BTCUSDT"))
        print(self.__client.book_ticker(symbols=["ETHUSDT", "BNBUSDT"]))

    def depth(self):
        print(self.__client.depth(symbol="ETHUSDT", limit=10))

    def exchange_info(self):
        print(self.__client.exchange_info(symbols=["BNBUSDT"]))

    def historical_trades(self):
        pass

    def kLines(self):
        print(self.__client.klines(symbol="BTCUSDT", interval="1h", limit=10))

    def ping(self):
        print(self.__client.ping())

    def rolling_window_ticker(self):
        print(self.__client.rolling_window_ticker(symbol="BNBUSDT", windowSize="1d", type="MINI"))

    def ticker_24hr(self):
        print(self.__client.ticker_24hr(symbols=['ETHBUSD'], type="FULL"))

    def ticker_price(self):
        print(self.__client.ticker_price(symbols=["BTCUSDT", "BNBUSDT"]))

    def time(self):
        print(self.__client.time())

    def trades(self):
        print(self.__client.trades(symbol="BTCUSDT", limit=10))

    def uikLines(self):
        print(self.__client.ui_klines(symbol="BTCUSDT", interval="1h", limit=10))


    def spot_tickers(self) -> List[str] | Exception:
        try:
            return list(map(lambda x: x.get('symbol'), self.__client.ticker_price()))
        except Exception as err:
            raise err

#2
    # def make_kLines(self) -> List[List[str]]:
    #     r = self.__client.klines("BTCUSDT", "1h", limit=300)
    #     df = self.make_dataFrame(r).iloc[:, :5]
    #     df.columns = ["ticker", "open", "high", "low", "close"]
    #     log.logger.info((df.tail(10)))
    #     return df
# #3
#     def make_MAFast_MASLow(self) -> List[List[str]]:
#         df = self.make_klines()
#         df['ma_fast'] = df['c'].ewm(span=12, adjust=False).mean()
#         df['ma_slow'] = df['c'].ewm(span=26, adjust=False).mean()
#         log.logger.info(df.tail(10))
#         return df

if __name__=='__main__':
    b = BinanceSpot()
    # b.agg_trades()
    # b.avg_price()
    # b.book_ticker()
    # b.depth()
    # b.exchange_info()
    # b.kLines()
    # b.ping()
    # b.rolling_window_ticker()
    # b.ticker_24hr()
    # b.ticker_price()
    # b.time()
    # b.trades()
    # b.uikLines()