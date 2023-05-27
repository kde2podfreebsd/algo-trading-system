import pytest

from Exchanges.Binance.Spot.Market import BinanceSpotMarket


@pytest.fixture()
def set_up():
    b = BinanceSpotMarket()
    return b
