import pytest

from ExchangesAPI.Binance import BinanceSpotMarket


@pytest.fixture()
def set_up():
    b = BinanceSpotMarket()
    return b
