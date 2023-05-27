from abc import ABC

import talib
from pandas.core.frame import DataFrame

from TaLib.TAInterface import TAInterface


class VolumeIndicators(TAInterface, ABC):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def AD(df: DataFrame):
        output = df
        output["AD"] = talib.AD(df["High"], df["Low"], df["Close"], df["Volume"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ADOSC(df: DataFrame, fastperiod: int, slowperiod: int):
        output = df
        output[f"ADOSC {fastperiod} {slowperiod}"] = talib.ADOSC(
            df["High"],
            df["Low"],
            df["Close"],
            df["Volume"],
            fastperiod=fastperiod,
            slowperiod=slowperiod,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def OBV(df: DataFrame):
        output = df
        output["OBV"] = talib.OBV(df["Close"], df["Volume"])
        return output
