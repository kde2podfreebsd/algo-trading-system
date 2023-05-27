import pytest

from ExchangesAPI.Binance.Spot import Market


@pytest.fixture()
def set_up():
    b = BinanceSpotMarket()
    return b
