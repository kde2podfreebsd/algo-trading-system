# import json
from datetime import datetime

from Exchanges.Binance.Spot.Market import BinanceSpotMarket
from TaLib.Modules.MomentumIndicators import MomentumIndicators
from TaLib.TAInterface import TAInterface

# from app.Exceptions import TaLibBaseException
# import numpy as np
# from pandas import DataFrame


class StrategyTester(TAInterface):
    def __init__(
        self,
        start_fiat_balance: float,
        start_coin_balance: str,
        coint_ticker: str,
        fiat_tikcer: str,
        bar_interval: str,
        startTime: datetime = None,
        endTime: datetime = None,
    ):
        self._fiat_balance = start_fiat_balance
        self._coin_balance = start_coin_balance
        self._ticker = coint_ticker
        self._fiat_tikcer = fiat_tikcer
        self.binanceSM = BinanceSpotMarket()
        self.mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
        self.df = self.binanceSM.makeKLinesDataFrame(
            symbol=coint_ticker,
            bar_interval=bar_interval,
            startTime=startTime,
            endTime=endTime,
        )
        self.buy_signal_price = []
        self.sell_signal_price = []
        self.data = {
            "Strategy": "___",
            "Bar Interval": bar_interval,
            "Start Time": startTime,
            "End Time": endTime,
            "start_coin_balance": start_coin_balance,
            "start_fiat_balance": start_fiat_balance,
            "End_coin_balance": None,
            "End_fiat_balance": None,
            "Profit": None,
            "Profit %": None,
            "Actions": [],
        }

    # def checkFiatBalanceForBuy(self, func):
    #     def wrapper(*args, **kwargs):
    #         if kwargs.get("fiat_amount") is not None:
    #             if kwargs.get("fiat_amount") < self._fiat_balance:
    #                 raise TaLibBaseException(err="Not have balance for this transaction")
    #
    #         result = func(**kwargs)
    #         return result
    #
    #     return wrapper

    def BUY(self, fiat_amount: float, iteration: int):
        self._coin_balance += float(fiat_amount) / float(self.df["Close"][iteration])
        self._fiat_balance -= float(fiat_amount)
        self.data["Actions"].append(
            f"[{self.df['Open time'][iteration]}] BUY {float(fiat_amount) / float(self.df['Close'][iteration])} {self._ticker} for {fiat_amount} {self._fiat_tikcer}"
        )

    def SELL(self, coin_amount: float, iteration: int):
        self._fiat_balance += float(coin_amount) * float(self.df["Close"][iteration])
        self._coin_balance -= float(coin_amount)
        self.data["Actions"].append(
            f"[{self.df['Open time'][iteration]}] SELL {coin_amount} {self._ticker} for {float(coin_amount) * float(self.df['Close'][iteration])} {self._ticker}"
        )

    # def StrategyLog(self):
