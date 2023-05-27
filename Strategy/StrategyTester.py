# import datetime
# import json
from datetime import datetime

# from settings import basedir


class StrategyTester:

    __Balance: float
    endTime: datetime
    coinTicker: str
    fiatTicker: str
    startFiatBalance: float
    startCoinBalance: float
    ticker: str
    startTime: datetime

    def __init__(
        self,
        ticker: str,
        start_fiat_balance: float,
        start_coin_balance: float,
        fiat_ticker: str,
        coin_ticker: str,
        startTime: datetime.datetime,
        endTime: datetime.datetime,
    ):
        self.ticker = ticker
        self.startFiatBalance = start_fiat_balance
        self.startCoinBalance = start_coin_balance
        self.fiatTicker = fiat_ticker
        self.coinTicker = coin_ticker
        self.startTime = startTime
        self.endTime = endTime
        self.__Balance = 0

    @property
    def Balance(self):
        return self.__Balance

    @Balance.setter
    def Balance(self, value):
        self.__Balance = value
