from app.TaLib.TABase import TAInterface
from pandas.core.frame import DataFrame
import talib

class OverlapStudies(TAInterface):

    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def BBANDS(df: DataFrame, timeperiod) -> DataFrame:
        dataframe = df
        c1, c2, c3 = f'upper_band {timeperiod}', f'middle_band {timeperiod}', f'lower_band {timeperiod}'
        dataframe[c1], dataframe[c2], dataframe[c3] = talib.BBANDS(df['Close price'], timeperiod=timeperiod)
        return dataframe

    @staticmethod
    def DEMA():
        pass

    @staticmethod
    def EMA(df: DataFrame, timeperiod: int) -> DataFrame:
        dataframe = df
        column_name = f'EMA {timeperiod}'
        dataframe[column_name] = talib.EMA(df['Close price'], timeperiod=timeperiod)
        return dataframe

    @staticmethod
    def HT_TRENDLINE():
        pass

    @staticmethod
    def KAMA():
        pass

    @staticmethod
    def MA():
        pass

    @staticmethod
    def MAMA():
        pass

    @staticmethod
    def MAVP():
        pass

    @staticmethod
    def MIDPOINT():
        pass

    @staticmethod
    def MIDPRICE():
        pass

    @staticmethod
    def SAR():
        pass

    @staticmethod
    def SAREXT():
        pass

    @staticmethod
    def SMA(df: DataFrame, timeperiod: int) -> DataFrame:
        dataframe = df
        column_name = f'SMA {timeperiod}'
        dataframe[column_name] = talib.SMA(df['Close price'], timeperiod=timeperiod)
        return dataframe

    @staticmethod
    def T3():
        pass

    @staticmethod
    def TEMA():
        pass

    @staticmethod
    def TRIMA():
        pass

    @staticmethod
    def WMA():
        pass