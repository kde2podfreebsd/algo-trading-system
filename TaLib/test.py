from TAInterface import TAInterface

from ExchangesAPI.Binance import BinanceSpotMarket
from TaLib.Modules.MomentumIndicators import MomentumIndicators

b = BinanceSpotMarket()
mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
df = b.makeKLinesDataFrame(
    symbol="BTCUSDT", bar_interval="1h", startTime=None, endTime=None
)


@TAInterface.is_valid_dataframe
def ta(df):
    return df


# ta(df=df)


# o = mi.ADX(df=df, timeperiod=14)
# o = mi.ADXR(df=df, timeperiod=14)
# o = mi.APO(df=df, fastperiod=12, slowperiod=26, matype=0)
# o = mi.AROON(df=df, timeperiod=14)
# o = mi.AROONOSC(df=df, timeperiod=14)
# o = mi.BOP(df=df)
# o = mi.CCI(df=df, timeperiod=14)
# o = mi.CMO(df=df,timeperiod=14)
# o = mi.DX(df=df,timeperiod=14)
# o = mi.MACD(df=df,fastperiod=12, slowperiod=26, signalperiod=9)
# o = mi.MACDEXT(df=df,fastperiod=12, fastmatype=0,slowperiod=26,slowmatype=0,signalperiod=9,signalmatype=0)
# o = mi.MACDFIX(df=df,signalperiod=9)
# o = mi.MFI(df=df, timeperiod=14)
# o = mi.MINUS_DI(df=df, timeperiod=14)
# o = mi.MINUS_DM(df=df,timeperiod=14)
# o = mi.MOM(df=df,timeperiod=10)
# o = mi.PLUS_DI(df=df,timeperiod=14)
# o = mi.PLUS_DM(df=df,timeperiod=14)
# o = mi.PPO(df=df,fastperiod=12,slowperiod=26,matype=0)
# o = mi.ROC(df=df,timeperiod=10)
# o = mi.ROCR(df=df,timeperiod=10)
# o = mi.ROCR100(df=df,timeperiod=10)
# o = mi.RSI(df=df,timeperiod=14)
# o = mi.STOCH(df=df,fastk_period=5,slowk_period=3,slowk_matype=0,slowd_period=3,slowd_matype=0)
# o = mi.STOCHF(df=df,fastk_period=5,fastd_period=3,fastd_matype=0)
# o = mi.STOCHRSI(df=df,timeperiod=14,fastk_period=5,fastd_period=3,fastd_matype=0)
# o = mi.TRIX(df=df,timeperiod=30)
# o = mi.ULTOSC(df=df,timeperiod1=7,timeperiod2=14,timeperiod3=28)
# o = mi.WILLR(df=df,timeperiod=14)
# print(o.tail(10))
# # ms = abstract.CDLMORNINGSTAR(data)
# # print(ms[ms!=0])
