from abc import ABC

import talib
from pandas.core.frame import DataFrame

from TaLib.TAInterface import TAInterface


class CycleIndicators(TAInterface, ABC):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def HT_DCPERIOD(df: DataFrame) -> DataFrame:
        output = df
        output["HT_DCPERIOD"] = talib.HT_DCPERIOD(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def HT_DCPHASE(df: DataFrame) -> DataFrame:
        output = df
        output["HT_DCPHASE"] = talib.HT_DCPHASE(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def HT_PHASOR(df: DataFrame) -> DataFrame:
        output = df
        (
            output["inphase"],
            output["quadrature"],
        ) = talib.HT_PHASOR(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def HT_SINE(df: DataFrame) -> DataFrame:
        output = df
        (output["sine"], output["leadsine"]) = talib.HT_SINE(df["Close"])
        return output


# не выводит integer
#     @staticmethod
#     @TAInterface.is_valid_dataframe
#     def HT_TRENDMODE(df: DataFrame):
#         output = df
#         output['HT_TRENDMODE'] = talib.HT_TRENDMODE(df['Close'])
#         return output
