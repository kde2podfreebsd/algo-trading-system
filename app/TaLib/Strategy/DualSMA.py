from datetime import datetime

import numpy as np

from app.BinanceSDK.BinanceSpotMarket import BinanceSpotMarket
from app.singletonWrapper import singleton
from app.TaLib.Modules.MomentumIndicators import MomentumIndicators
from app.TaLib.Modules.OverlapStudies import OverlapStudies


@singleton
class DualSMA_strategy(object):
    def __init__(self, ticker: str):
        self.binanceSM = BinanceSpotMarket()
        self.mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
        self.os = OverlapStudies(max_rows=1000, max_columns=1000, width=1000)
        self.df = self.binanceSM.makeKLinesDataFrame(
            symbol=ticker,
            bar_interval="1h",
            startTime=datetime(2022, 1, 1),
            endTime=None,
        )
        self.balance = 0
        self.coin = 0.000036

    def Main(self):

        self.df = self.os.SMA(df=self.df, timeperiod=10)
        self.df = self.os.SMA(df=self.df, timeperiod=50)

        buy_signal_price = []
        sell_signal_price = []
        flag = 0

        for i in range(len(self.df)):
            if self.df["SMA 10"][i] > self.df["SMA 50"][i]:
                if flag != 1:
                    buy_signal_price.append(self.df["Close"][i])
                    sell_signal_price.append(np.nan)
                    flag = 1
                else:
                    buy_signal_price.append(np.nan)
                    sell_signal_price.append(np.nan)

            elif self.df["SMA 10"][i] < self.df["SMA 50"][i]:
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

        self.df["DUALSMA_BUY_SIGNAL"] = buy_signal_price
        self.df["DUALSMA_SELL_SIGNAL"] = sell_signal_price

        print(self.df["DUALSMA_SELL_SIGNAL"][self.df["DUALSMA_SELL_SIGNAL"] != np.nan])

        # print(self.df.tail(10))

        return self.df

    def test_with_balance(self):

        start_balance = self.balance + (float(self.coin) * float(self.df["Close"][0]))

        self.df = self.os.SMA(df=self.df, timeperiod=10)
        self.df = self.os.SMA(df=self.df, timeperiod=50)

        buy_signal_price = []
        sell_signal_price = []
        flag = 0

        for i in range(len(self.df)):
            if self.df["SMA 10"][i] > self.df["SMA 50"][i]:
                if flag != 1:
                    buy_signal_price.append(self.df["Close"][i])
                    self.coin = float(self.balance) / float(self.df["Close"][i])
                    print(f"[{i}] Buy {self.coin} BTC for {self.balance}")
                    self.balance -= self.balance
                    sell_signal_price.append(np.nan)
                    flag = 1
                    print(
                        f"[{i}] Balance: {self.balance} | Coin: {self.coin} | Flag = 1: BUY\n\n"
                    )
                else:
                    buy_signal_price.append(np.nan)
                    sell_signal_price.append(np.nan)

            elif self.df["SMA 10"][i] < self.df["SMA 50"][i]:
                if flag != -1:
                    sell_signal_price.append(self.df["Close"][i])
                    buy_signal_price.append(np.nan)
                    self.balance = float(self.coin) * float(self.df["Close"][i])
                    print(f"[{i}] Sell {self.coin} BTC for {self.balance}")
                    self.coin -= self.coin
                    flag = -1
                    print(
                        f"[{i}] Balance: {self.balance} | Coin: {self.coin} | Flag = -1: SELL\n\n"
                    )
                else:
                    buy_signal_price.append(np.nan)
                    sell_signal_price.append(np.nan)

            else:
                buy_signal_price.append(np.nan)
                sell_signal_price.append(np.nan)

        # self.df['DUALSMA_BUY_SIGNAL'] = buy_signal_price
        # self.df['DUALSMA_SELL_SIGNAL'] = sell_signal_price

        # print(self.df['DUALSMA_SELL_SIGNAL'][self.df['DUALSMA_SELL_SIGNAL'] != np.nan])

        # print(self.df.tail(10))

        print(start_balance)
        print(self.balance, self.coin)
        profit = (self.balance / start_balance) - 1
        print(f"Profit: {profit * 100}%")
        print(
            f'Time: {self.df["Open time"][0]} --------> {self.df["Open time"].tail(1).values[0]}'
        )
        return self.df


d = DualSMA_strategy(ticker="BTCUSDT")
# print(d.Main())
d.test_with_balance()
