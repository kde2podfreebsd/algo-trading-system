# import json
import numpy as np

from app.BinanceSDK.BinanceSpotMarket import BinanceSpotMarket
from app.TaLib.Modules.MomentumIndicators import MomentumIndicators

# from app.settings import basedir


class MACDBase_strategy(object):
    def __init__(self, ticker: str):
        self.binanceSM = BinanceSpotMarket()
        self.mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
        self.df = self.binanceSM.makeKLinesDataFrame(
            symbol=ticker, bar_interval="30m", startTime=None, endTime=None
        )
        self.balance = 0
        self.coin = 0.0036

    def Main(self):
        print(self.df)
        self.df = self.mi.MACD(df=self.df, fastperiod=12, slowperiod=26, signalperiod=9)
        print(self.df[["MACD 12 26 9", "MACD signal 12 26 9"]])

        buy_signal_price = []
        sell_signal_price = []
        flag = 0

        for i in range(len(self.df)):
            if self.df["MACD 12 26 9"][i] > self.df["MACD signal 12 26 9"][i]:
                if flag != 1:
                    buy_signal_price.append(self.df["Close"][i])
                    sell_signal_price.append(np.nan)
                    flag = 1
                else:
                    buy_signal_price.append(np.nan)
                    sell_signal_price.append(np.nan)

            elif self.df["MACD 12 26 9"][i] < self.df["MACD signal 12 26 9"][i]:
                if flag != -1:
                    sell_signal_price.append(self.df["Close"][i])
                    buy_signal_price.append(np.nan)
                    flag = -1
                else:
                    buy_signal_price.append(np.nan)
                    sell_signal_price.append(np.nan)

            else:
                buy_signal_price.append(np.nan)
                sell_signal_price.append(np.nan)

        self.df["MACDBase_BUY_SIGNAL"] = buy_signal_price
        self.df["MACDBase_SELL_SIGNAL"] = sell_signal_price

        return self.df


mb = MACDBase_strategy(ticker="BTCUSDT")
mb.Main()
