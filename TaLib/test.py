from TAInterface import TAInterface

from Exchanges.Binance.Spot.Market import BinanceSpotMarket
from TaLib.Modules.CycleIndicators import CycleIndicators
from TaLib.Modules.MathOperators import MathOperators
from TaLib.Modules.MathTransform import MathTransform
from TaLib.Modules.MomentumIndicators import MomentumIndicators
from TaLib.Modules.OverlapStudies import OverlapStudies
from TaLib.Modules.PatternRecognition import PatternRecognition
from TaLib.Modules.PriceTransform import PriceTransform
from TaLib.Modules.StatisticFunctions import StatisticFunctions
from TaLib.Modules.VolatilityIndicators import VolatilityIndicators
from TaLib.Modules.VolumeIndicators import VolumeIndicators

# import talib

b = BinanceSpotMarket()
mi = MomentumIndicators(max_rows=1000, max_columns=1000, width=1000)
ci = CycleIndicators(max_rows=1000, max_columns=1000, width=1000)
mo = MathOperators(max_rows=1000, max_columns=1000, width=1000)
mt = MathTransform(max_rows=1000, max_columns=1000, width=1000)
os = OverlapStudies(max_rows=1000, max_columns=1000, width=1000)
pr = PatternRecognition(max_rows=1000, max_columns=1000, width=1000)
pt = PriceTransform(max_rows=1000, max_columns=1000, width=1000)
sf = StatisticFunctions(max_rows=1000, max_columns=1000, width=1000)
volatind = VolatilityIndicators(max_rows=1000, max_columns=1000, width=1000)
volumeind = VolumeIndicators(max_rows=1000, max_columns=1000, width=1000)
df = b.makeKLinesDataFrame(
    symbol="BTCUSDT", bar_interval="1h", startTime=None, endTime=None
)


@TAInterface.is_valid_dataframe
def ta(df):
    return df


# ta(df=df)

# CycleIndicators
# o = ci.HT_DCPERIOD(df=df)
# o = ci.HT_DCPHASE(df=df)
# o = ci.HT_PHASOR(df=df)
# o = ci.HT_SINE(df=df)
# o = ci.HT_TRENDMODE(df=df)

# MathOperators
# o = mo.ADD(df=df)
# o = mo.DIV(df=df)
# o = mo.MAX(df=df, timeperiod=30)
# o = mo.MAXINDEX(df=df, timeperiod=30)
# o = mo.MIN(df=df, timeperiod=30)
# o = mo.MININDEX(df=df, timeperiod=30)
# o = mo.MINMAX(df=df, timeperiod=30)
# o = mo.MINMAXINDEX(df=df, timeperiod=30)
# o = mo.MULT(df=df)
# o = mo.SUB(df=df)
# o = mo.SUM(df=df, timeperiod=30)

# MathTransform
# o = mt.ACOS(df=df)
# o = mt.ASIN(df=df)
# o = mt.ATAN(df=df)
# o = mt.CEIL(df=df)
# o = mt.COS(df=df)
# o = mt.COSH(df=df)
# o = mt.EXP(df=df)
# o = mt.FLOOR(df=df)
# o = mt.LN(df=df)
# o = mt.LOG10(df=df)
# o = mt.SIN(df=df)
# o = mt.SINH(df=df)
# o = mt.SQRT(df=df)
# o = mt.TAN(df=df)
# o = mt.TANH(df=df)

# MomentumIndicators
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

# OverlapStudies
# o = os.BBANDS(df=df, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
# o = os.DEMA(df=df, timeperiod=30)
# o = os.EMA(df=df, timeperiod=30)
# o = os.HT_TRENDLINE(df=df)
# o = os.KAMA(df=df, timeperiod=30)
# o = os.MA(df=df, timeperiod=30, matype=0)
# o = os.MAMA(df=df, fastlimit=0.5, slowlimit=0.05)
# o = os.MAVP(df=df...)
# o = os.MIDPOINT(df=df, timeperiod=14)
# o = os.MIDPRICE(df=df, timeperiod=14)
# o = os.SAR(df=df, acceleration=0.02, maximum=0.2)
# o = os.SAREXT(df=df, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02, accelerationlong=0.02, accelerationmaxlong=0.2, accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.2)
# o = os.SMA(df=df, timeperiod=30)
# o = os.T3(df=df, timeperiod=5, vfactor=0.7)
# o = os.TEMA(df=df, timeperiod=30)
# o = os.TRIMA(df=df, timeperiod=30)
# o = os.WMA(df=df, timeperiod=30)

# PatternRecognition
# o = pr.CDL2CROWS(df=df)
# o = pr.CDL3BLACKCROWS(df=df)
# o = pr.CDL3INSIDE(df=df)
# o = pr.CDL3LINESTRIKE(df=df)
# o = pr.CDL3OUTSIDE(df=df)
# o = pr.CDL3STARSINSOUTH(df=df)
# o = pr.CDL3WHITESOLDIERS(df=df)
# o = pr.CDLABANDONEDBABY(df=df, penetration=0.3)
# o = pr.CDLADVANCEBLOCK(df=df)
# o = pr.CDLBELTHOLD(df=df)
# o = pr.CDLBREAKAWAY(df=df)
# o = pr.CDLCLOSINGMARUBOZU(df=df)
# o = pr.CDLCONCEALBABYSWALL(df=df)
# o = pr.CDLCOUNTERATTACK(df=df)
# o = pr.CDLDARKCLOUDCOVER(df=df, penetration=0.5)
# o = pr.CDLDOJI(df=df)
# o = pr.CDLDOJISTAR(df=df)
# o = pr.CDLDRAGONFLYDOJI(df=df)
# o = pr.CDLENGULFING(df=df)


# PriceTransform
# o = pt.AVGPRICE(df=df)
# o = pt.MEDPRICE(df=df)
# o = pt.TYPPRICE(df=df)
# o = pt.WCLPRICE(df=df)

# StatisticFunctions
# o = sf.BETA(df=df, timeperiod=5)
# o = sf.CORREL(df=df, timeperiod=30)
# o = sf.LINEARREG(df=df, timeperiod=14)
# o = sf.LINEARREG_ANGLE(df=df, timeperiod=14)
# o = sf.LINEARREG_INTERCEPT(df=df, timeperiod=14)
# o = sf.LINEARREG_SLOPE(df=df, timeperiod=14)
# o = sf.STDDEV(df=df, timeperiod=5, nbdev=1)
# o = sf.TSF(df=df, timeperiod=14)
# o = sf.VAR(df=df, timeperiod=5, nbdev=1)

# VolatilityIndicators
# o = volatind.ATR(df=df, timeperiod=14)
# o = volatind.NATR(df=df, timeperiod=14)
# o = volatind.TRANGE(df=df)

# VolumeIndicators
# o = volumeind.AD(df=df)
# o = volumeind.ADOSC(df=df, fastperiod=3, slowperiod=10)
# o = volumeind.OBV(df=df)

# print(o.tail(10))

# # ms = abstract.CDLMORNINGSTAR(data)
# # print(ms[ms!=0])
