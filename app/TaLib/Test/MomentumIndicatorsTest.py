import pytest
from app.TaLib.Modules.MomentumIndicators import MomentumIndicators
from app.BinanceSDK.BinanceSpotMarket import BinanceSpotMarket
from app.TaLib.Modules.MomentumIndicators import MomentumIndicators
from pandas import DataFrame


@pytest.fixture()
def set_up():
    b = BinanceSpotMarket()
    mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
    df = b.makeKLinesDataFrame(symbol='BTCUSDT', bar_interval='1h', startTime=None, endTime=None)

    return mi, df

def test1_ADX(set_up):
    mi, df = set_up
    output = mi.ADX(df=df, timeperiod=14)
    assert isinstance(output, DataFrame)

def test2_ADXR(set_up):
    mi, df = set_up
    output = mi.ADXR(df=df, timeperiod=14)
    assert isinstance(output, DataFrame)

def test3_APO(set_up):
    mi, df = set_up
    output = mi.APO(df=df, fastperiod=12, slowperiod=26, matype=0)
    assert isinstance(output, DataFrame)

def test4__AROON(set_up):
    mi, df = set_up
    output = mi.AROON(df=df, timeperiod=14)
    assert isinstance(output, DataFrame)
