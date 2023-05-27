from abc import ABC

import talib
from pandas.core.frame import DataFrame

from TaLib.TAInterface import TAInterface


class MathOperators(TAInterface, ABC):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ADD(df: DataFrame) -> DataFrame:
        output = df
        output["ADD"] = talib.ADD(
            df["High"],
            df["Low"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def DIV(df: DataFrame) -> DataFrame:
        output = df
        output["DIV"] = talib.DIV(
            df["High"],
            df["Low"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MAX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MAX {timeperiod}"] = talib.MAX(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MAXINDEX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MAXINDEX {timeperiod}"] = talib.MAXINDEX(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MIN(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MIN {timeperiod}"] = talib.MIN(df["Close"], timeperiod=timeperiod)
        return output

    # OUTPUT - integer (спросить)
    @staticmethod
    @TAInterface.is_valid_dataframe
    def MININDEX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MININDEX {timeperiod}"] = talib.MININDEX(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MINMAX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        (
            output["min"],
            output["max"],
        ) = talib.MINMAX(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MINMAXINDEX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        (
            output["minidx"],
            output["maxidx"],
        ) = talib.MINMAXINDEX(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MULT(df: DataFrame) -> DataFrame:
        output = df
        output["MULT"] = talib.MULT(
            df["High"],
            df["Low"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SUB(df: DataFrame) -> DataFrame:
        output = df
        output["SUB"] = talib.SUB(
            df["High"],
            df["Low"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SUM(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output["SUM"] = talib.SUM(df["Close"], timeperiod=timeperiod)
        return output
