from pandas.core.frame import DataFrame

import talib
from TaLib.TAInterface import TAInterface


class OverlapStudies(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def BBANDS(
        df: DataFrame, timeperiod: int, nbdevup: int, nbdevdn: int, matype: int
    ) -> DataFrame:
        output = df
        (
            output[f"upperband {timeperiod} {nbdevup} {nbdevdn} {matype}"],
            output[f"middleband {timeperiod} {nbdevup} {nbdevdn} {matype}"],
            output[f"lowerband {timeperiod} {nbdevup} {nbdevdn} {matype}"],
        ) = talib.BBANDS(
            df["Close"],
            timeperiod=timeperiod,
            nbdevup=nbdevup,
            nbdevdn=nbdevdn,
            matype=matype,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def DEMA(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output["DEMA"] = talib.DEMA(df["Close"], timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def EMA(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"EMA {timeperiod}"] = talib.EMA(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def HT_TRENDLINE(df: DataFrame) -> DataFrame:
        output = df
        output["HT_TRENDLINE"] = talib.HT_TRENDLINE(df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def KAMA(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"KAMA {timeperiod}"] = talib.KAMA(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MA(df: DataFrame, timeperiod: int, matype: int) -> DataFrame:
        output = df
        output[f"MA {timeperiod} {matype}"] = talib.MA(
            df["Close"],
            timeperiod=timeperiod,
            matype=matype,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MAMA(df: DataFrame, fastlimit: float, slowlimit: float) -> DataFrame:
        output = df
        (
            output[f"mama {fastlimit} {slowlimit}"],
            output[f"fama {fastlimit} {slowlimit}"],
        ) = talib.MAMA(
            df["Close"],
            fastlimit=fastlimit,
            slowlimit=slowlimit,
        )
        return output

    # #узнать, что такое periods
    #     @staticmethod
    #     @TAInterface.is_valid_dataframe
    #     def MAVP(df: DataFrame):
    #         output = df

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MIDPOINT(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MIDPOINT {timeperiod}"] = talib.MIDPOINT(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MIDPRICE(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MIDPRICE {timeperiod}"] = talib.MIDPRICE(
            df["High"],
            df["Low"],
            timeperiod=timeperiod,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SAR(df: DataFrame, acceleration: float, maximum: float) -> DataFrame:
        output = df
        output["SAR"] = talib.SAR(
            df["High"],
            df["Low"],
            acceleration=acceleration,
            maximum=maximum,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SAREXT(
        df: DataFrame,
        startvalue: int,
        offsetonreverse: int,
        accelerationinitlong: float,
        accelerationlong: float,
        accelerationmaxlong: float,
        accelerationinitshort: float,
        accelerationshort: float,
        accelerationmaxshort: float,
    ) -> DataFrame:
        output = df
        output["SAREXT"] = talib.SAREXT(
            df["High"],
            df["Low"],
            startvalue=startvalue,
            offsetonreverse=offsetonreverse,
            accelerationinitlong=accelerationinitlong,
            accelerationlong=accelerationlong,
            accelerationmaxlong=accelerationmaxlong,
            accelerationinitshort=accelerationinitshort,
            accelerationshort=accelerationshort,
            accelerationmaxshort=accelerationmaxshort,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def SMA(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"SMA {timeperiod}"] = talib.SMA(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def T3(df: DataFrame, timeperiod: int, vfactor: float) -> DataFrame:
        output = df
        output[f"T3 {timeperiod}"] = talib.T3(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def TEMA(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"TEMA {timeperiod}"] = talib.TEMA(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def TRIMA(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"TRIMA {timeperiod}"] = talib.TRIMA(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def WMA(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"WMA {timeperiod}"] = talib.WMA(df["Close"], timeperiod=timeperiod)
        return output
