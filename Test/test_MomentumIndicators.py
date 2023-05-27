import pytest
from pandas import DataFrame

from Exchanges.Binance.Spot.Market import BinanceSpotMarket
from TaLib.Modules.MomentumIndicators import MomentumIndicators


@pytest.fixture()
def set_up():
    b = BinanceSpotMarket()
    mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
    df = b.makeKLinesDataFrame(
        symbol="BTCUSDT", bar_interval="1h", startTime=None, endTime=None
    )

    return mi, df


@pytest.fixture()
def period_12d():
    return 12


@pytest.fixture()
def period_14d():
    return 14


@pytest.fixture()
def period_26d():
    return 26


@pytest.mark.parametrize(
    "timeperiod",
    [("period_12d"), ("period_14d"), ("period_26d")],
)
def test1_ADX(set_up, timeperiod, request):
    timeperiod = request.getfixturevalue(timeperiod)
    mi, df = set_up
    output = mi.ADX(df=df, timeperiod=timeperiod)
    assert isinstance(output, DataFrame)


@pytest.mark.parametrize(
    "timeperiod",
    [("period_12d"), ("period_14d"), ("period_26d")],
)
def test2_ADXR(set_up, timeperiod, request):
    timeperiod = request.getfixturevalue(timeperiod)
    mi, df = set_up
    output = mi.ADXR(df=df, timeperiod=timeperiod)
    assert isinstance(output, DataFrame)


@pytest.mark.parametrize(
    "fastperiod,slowperiod",
    [("period_12d", "period_14d"), ("period_14d", "period_26d")],
)
def test3_APO(set_up, fastperiod, slowperiod, request):
    fastperiod = request.getfixturevalue(fastperiod)
    slowperiod = request.getfixturevalue(slowperiod)
    mi, df = set_up
    output = mi.APO(df=df, fastperiod=fastperiod, slowperiod=slowperiod, matype=0)
    assert isinstance(output, DataFrame)


@pytest.mark.parametrize(
    "timeperiod",
    [("period_12d"), ("period_14d"), ("period_26d")],
)
def test4__AROON(set_up, timeperiod, request):
    timeperiod = request.getfixturevalue(timeperiod)
    mi, df = set_up
    output = mi.AROON(df=df, timeperiod=timeperiod)
    assert isinstance(output, DataFrame)
