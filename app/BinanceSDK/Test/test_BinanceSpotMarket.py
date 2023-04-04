import pytest

from app.BinanceSDK.BinanceSpotMarket import BinanceSpotMarket


@pytest.fixture()
def set_up():
    b = BinanceSpotMarket()
    return b
