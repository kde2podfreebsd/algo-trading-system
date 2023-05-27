from abc import ABC

import talib
from pandas.core.frame import DataFrame

from TaLib.TAInterface import TAInterface


class PriceTransform(TAInterface, ABC):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def AVGPRICE(df: DataFrame):
        output = df
        output["AVGPRICE"] = talib.AVGPRICE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MEDPRICE(df: DataFrame):
        output = df
        output["MEDPRICE"] = talib.MEDPRICE(
            df["High"],
            df["Low"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def TYPPRICE(df: DataFrame):
        output = df
        output["TYPPRICE"] = talib.TYPPRICE(
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def WCLPRICE(df: DataFrame):
        output = df
        output["WCLPRICE"] = talib.WCLPRICE(
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output
