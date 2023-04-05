# import datetime
import json

import numpy as np

from app.BinanceSDK.BinanceSpotMarket import BinanceSpotMarket
from app.setup_logger import basedir
from app.singletonWrapper import singleton
from app.TaLib.Modules.MomentumIndicators import MomentumIndicators
from app.TaLib.Modules.OverlapStudies import OverlapStudies

# import time


@singleton
class DualSMA_strategy(object):
    def __init__(self, ticker: str):
        self.binanceSM = BinanceSpotMarket()
        self.mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
        self.os = OverlapStudies(max_rows=1000, max_columns=1000, width=1000)
        self.df = self.binanceSM.makeKLinesDataFrame(
            symbol=ticker, bar_interval="1h", startTime=None, endTime=None
        )
        self.balance = 0
        self.coin = 0.0036

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

        return self.df

    def test_with_balance(
        self,
        output_file=f"{basedir}/TaLib/Strategy/Logs/DualSMA__1h__2023_03_01__2023_04_04.json",
    ):

        start_balance = self.balance + (float(self.coin) * float(self.df["Close"][0]))

        with open(output_file, "w") as outfile:
            pass

        data = {
            "Strategy": "DualSMA",
            "Bar Interval": "1 Hour",
            "Start Time": "2023.03.01",
            "End Time": "2023.04.04",
            "Start Balance": start_balance,
            "End Balance": None,
            "Profit": None,
            "Profit %": None,
            "Actions": [],
        }

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
                    data["Actions"].append(
                        (f"[{i}] Buy {self.coin} BTC for {self.balance} USDT")
                    )
                    self.balance -= self.balance
                    sell_signal_price.append(np.nan)
                    flag = 1
                    print(
                        f"[{i}] Balance: {self.balance} | Coin: {self.coin} | Flag = 1: BUY"
                    )
                    data["Actions"].append(
                        f"[{i}] Balance: {self.balance} BTC | Coin: {self.coin} USDT | Flag = 1: BUY"
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
                    data["Actions"].append(
                        f"[{i}] Sell {self.coin} BTC for {self.balance} USDT"
                    )
                    self.coin -= self.coin
                    flag = -1
                    print(
                        f"[{i}] Balance: {self.balance} | Coin: {self.coin} | Flag = -1: SELL"
                    )
                    data["Actions"].append(
                        f"[{i}] Balance: {self.balance} BTC | Coin: {self.coin} USDT | Flag = -1: SELL"
                    )
                else:
                    buy_signal_price.append(np.nan)
                    sell_signal_price.append(np.nan)

            else:
                buy_signal_price.append(np.nan)
                sell_signal_price.append(np.nan)

        self.df["BUY"] = buy_signal_price
        self.df["SELL"] = sell_signal_price

        print(f"Start Balance: {start_balance}")
        print(self.balance, self.coin)
        self.balance += float(self.df["Close"].tail(1).values[0]) * self.coin
        profit = (self.balance / start_balance) - 1
        print(f"Profit: {profit * 100}%")
        print(
            f'Time: {self.df["Open time"][0]} --------> {self.df["Open time"].tail(1).values[0]}'
        )

        data["End Balance"] = self.balance
        data["Profit"] = self.balance - start_balance
        data["Profit %"] = f"{profit * 100} %"

        print(data)

        with open(output_file, "w") as outfile:
            json.dump(data, outfile, indent=2)

        return self.df


d = DualSMA_strategy(ticker="BTCUSDT")
d.test_with_balance()
