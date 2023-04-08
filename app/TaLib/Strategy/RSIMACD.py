# import json
# import numpy as np
from app.BinanceSDK.BinanceSpotMarket import BinanceSpotMarket
from app.singletonWrapper import singleton
from app.TaLib.Modules.MomentumIndicators import MomentumIndicators

# from app.settings import basedir


@singleton
class RSIMACD_strategy(object):
    def __init__(self, ticker: str):
        self.binanceSM = BinanceSpotMarket()
        self.mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
        self.df = self.binanceSM.makeKLinesDataFrame(
            symbol=ticker, bar_interval="1h", startTime=None, endTime=None
        )
        self.balance = 0
        self.coin = 0.0036

    def Main(self):
        print(self.df)
        self.df = self.mi.RSI(df=self.df, timeperiod=14)
        self.df = self.mi.MACD(df=self.df, fastperiod=12, slowperiod=26, signalperiod=9)
        print(self.df)


rm = RSIMACD_strategy(ticker="BTCUSDT")
rm.Main()
