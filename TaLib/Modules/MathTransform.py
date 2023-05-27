from pandas.core.frame import DataFrame

import talib
from TaLib.TAInterface import TAInterface


class MathTransform(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ACOS(df: DataFrame) -> DataFrame:
        output = df
        output["ACOS"] = talib.ACOS(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ASIN(df: DataFrame) -> DataFrame:
        output = df
        output["ASIN"] = talib.ASIN(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ATAN(df: DataFrame) -> DataFrame:
        output = df
        output["ATAN"] = talib.ATAN(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CEIL(df: DataFrame) -> DataFrame:
        output = df
        output["CEIL"] = talib.CEIL(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def COS(df: DataFrame) -> DataFrame:
        output = df
        output["COS"] = talib.COS(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def COSH(df: DataFrame) -> DataFrame:
        output = df
        output["COSH"] = talib.COSH(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def EXP(df: DataFrame) -> DataFrame:
        output = df
        output["EXP"] = talib.EXP(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def FLOOR(df: DataFrame) -> DataFrame:
        output = df
        output["FLOOR"] = talib.FLOOR(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def LN(df: DataFrame) -> DataFrame:
        output = df
        output["LN"] = talib.LN(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def LOG10(df: DataFrame) -> DataFrame:
        output = df
        output["LOG10"] = talib.LOG10(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SIN(df: DataFrame) -> DataFrame:
        output = df
        output["SIN"] = talib.SIN(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SINH(df: DataFrame) -> DataFrame:
        output = df
        output["SINH"] = talib.SINH(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SQRT(df: DataFrame) -> DataFrame:
        output = df
        output["SQRT"] = talib.SQRT(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def TAN(df: DataFrame) -> DataFrame:
        output = df
        output["TAN"] = talib.TAN(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def TANH(df: DataFrame) -> DataFrame:
        output = df
        output["TANH"] = talib.TANH(df["Close"])
        return output
