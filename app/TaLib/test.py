from app.BinanceSDK.SpotMarket.BinanceSpotMarketAdapter import BinanceSpotMarketAdapter
from datetime import datetime
import talib
# from app.TaLib.TA_Interface import TAInterface
import numpy as np

b = BinanceSpotMarketAdapter()

class C(TAInterface):
    pass

# df = b.makeKLinesDataFrame(symbol='BTCUSDT', bar_interval='1d', startTime=datetime(2023,4,3), endTime=None)
df = b.makeKLinesDataFrame(symbol='BTCUSDT', bar_interval='1h', startTime=None, endTime=None)
c = C()
# df = c.SMA_5_10_20_50_100_200(df=df)
# df = c.SMA_N(df=df, timeperiod=14)
# df= c.EMA_5_10_20_50_100_200(df=df)
# df = c.EMA_N(df=df, timeperiod=14)
# df = c.RSI_N(df=df, timeperiod=14)
# print(c.STOCH(df=df, fastk_period = 9, slowk_period = 6, slowk_matype = 0, slowd_period = 3, slowd_matype = 0))
# df = c.BollingerBands(df=df, timeperiod=14)
# df = c.MACD(df=df, fastperiod=12, slowperiod=25, signalperiod=9)
# df = c.FibonacciRetracements(df=df)
print(df)

# data.rename(columns={
#     'Open': 'open',
#     'High': 'high',
#     'Low': 'low',
#     'Adj Close': 'close',
#     'Volume': 'volume'
# }, inplace=True)

# ms = abstract.CDLMORNINGSTAR(data)
# print(ms[ms!=0])


