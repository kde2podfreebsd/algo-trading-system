from app.TaLib.TABase import TAInterface
import talib
from pandas.core.frame import DataFrame

class MomentumIndicators(TAInterface):

    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def ADX():
        pass

    @staticmethod
    def ADXR():
        pass

    @staticmethod
    def APO():
        pass

    @staticmethod
    def AROON():
        pass

    @staticmethod
    def AROONOSC():
        pass

    @staticmethod
    def BOP():
        pass

    @staticmethod
    def CCI():
        pass

    @staticmethod
    def CMO():
        pass

    @staticmethod
    def DX():
        pass

    @staticmethod
    def MACD(df: DataFrame, fastperiod: int, slowperiod: int, signalperiod: int):
        dataframe = df
        c1, c2, c3 = f'MACD {fastperiod} {slowperiod} {signalperiod}', f'MACD signal {fastperiod} {slowperiod} {signalperiod}', f' MACD hist {fastperiod} {slowperiod} {signalperiod}'
        dataframe[c1], dataframe[c2], dataframe[c3] = talib.MACD(df["Close price"], fastperiod=fastperiod,
                                                                 slowperiod=slowperiod, signalperiod=signalperiod)
        return dataframe

    @staticmethod
    def MACDEXT():
        pass

    @staticmethod
    def MACDFIX():
        pass

    @staticmethod
    def MFI():
        pass

    @staticmethod
    def MINUS_DI():
        pass

    @staticmethod
    def MINUS_DM():
        pass

    @staticmethod
    def MOM():
        pass

    @staticmethod
    def PLUS_DI():
        pass

    @staticmethod
    def PLUS_DM():
        pass

    @staticmethod
    def PPO():
        pass

    @staticmethod
    def ROC():
        pass

    @staticmethod
    def ROCP():
        pass

    @staticmethod
    def ROCR():
        pass

    @staticmethod
    def ROCR100():
        pass

    @staticmethod
    def RSI(df: DataFrame, timeperiod) -> DataFrame:
        dataframe = df
        column_name = f'RSI {timeperiod}'
        dataframe[column_name] = talib.RSI(df['Close price'], timeperiod=timeperiod)
        return dataframe


    @staticmethod
    def STOCH(df: DataFrame, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype) -> DataFrame:
        dataframe = df
        c1, c2 = f'STOCH_slowk {fastk_period} {slowk_period} {slowd_period}', f'STOCH_slowd {fastk_period} {slowk_period} {slowd_period}'
        dataframe[c1], dataframe[c2] = talib.STOCH(
            df['High price'],
            df['Close price'],
            df['Close price'],
            fastk_period=fastk_period,
            slowk_period=slowk_period,
            slowd_period=slowd_period,
            slowk_matype=slowk_matype,
            slowd_matype=slowd_matype
        )
        return dataframe

    @staticmethod
    def STOCHF():
        pass

    @staticmethod
    def STOCHRSI():
        pass

    @staticmethod
    def TRIX():
        pass

    @staticmethod
    def ULTOSC():
        pass

    @staticmethod
    def WILLR():
        pass