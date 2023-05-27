from abc import ABC

import talib
from pandas.core.frame import DataFrame

from TaLib.TAInterface import TAInterface


class StatisticFunctions(TAInterface, ABC):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def BETA(df: DataFrame, timeperiod: int):
        output = df
        output[f"BETA {timeperiod}"] = talib.BETA(
            df["High"], df["Low"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CORREL(df: DataFrame, timeperiod: int):
        output = df
        output[f"CORREL {timeperiod}"] = talib.CORREL(
            df["High"], df["Low"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def LINEARREG(df: DataFrame, timeperiod: int):
        output = df
        output[f"LINEARREG {timeperiod}"] = talib.LINEARREG(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def LINEARREG_ANGLE(df: DataFrame, timeperiod: int):
        output = df
        output[f"LINEARREG_ANGLE {timeperiod}"] = talib.LINEARREG_ANGLE(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def LINEARREG_INTERCEPT(df: DataFrame, timeperiod: int):
        output = df
        output[f"LINEARREG_INTERCEPT {timeperiod}"] = talib.LINEARREG_INTERCEPT(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def LINEARREG_SLOPE(df: DataFrame, timeperiod: int):
        output = df
        output[f"LINEARREG_SLOPE {timeperiod}"] = talib.LINEARREG_SLOPE(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def STDDEV(df: DataFrame, timeperiod: int, nbdev: float):
        output = df
        output[f"STDDEV {timeperiod}"] = talib.STDDEV(
            df["Close"],
            timeperiod=timeperiod,
            nbdev=nbdev,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def TSF(df: DataFrame, timeperiod: int):
        output = df
        output[f"TSF {timeperiod}"] = talib.TSF(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def VAR(df: DataFrame, timeperiod: int, nbdev: int):
        output = df
        output[f"VAR {timeperiod}"] = talib.VAR(
            df["Close"],
            timeperiod=timeperiod,
            nbdev=nbdev,
        )
        return output
