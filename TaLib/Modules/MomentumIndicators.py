from abc import ABC

import talib
from pandas.core.frame import DataFrame

from TaLib.TAInterface import TAInterface


class MomentumIndicators(TAInterface, ABC):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ADX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"ADX {timeperiod}"] = talib.ADX(
            df["High"], df["Low"], df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ADXR(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"ADRX {timeperiod}"] = talib.ADXR(
            df["High"], df["Low"], df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def APO(df: DataFrame, fastperiod: int, slowperiod: int, matype: int) -> DataFrame:
        output = df
        output[f"APO {fastperiod} {slowperiod}"] = talib.APO(
            df["Close"], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def AROON(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        (
            output[f"AROON_down {timeperiod}"],
            output[f"AROON_up {timeperiod}"],
        ) = talib.AROON(df["High"], df["Low"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def AROONOSC(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"AROONOSC {timeperiod}"] = talib.AROONOSC(
            df["High"], df["Low"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def BOP(df: DataFrame) -> DataFrame:
        output = df
        output["BOP"] = talib.BOP(df["Open"], df["High"], df["Low"], df["Close"])
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CCI(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"CCI {timeperiod}"] = talib.CCI(
            df["High"], df["Low"], df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CMO(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"CMO {timeperiod}"] = talib.CMO(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def DX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        df[f"DX {timeperiod}"] = talib.DX(
            df["High"], df["Low"], df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MACD(
        df: DataFrame, fastperiod: int, slowperiod: int, signalperiod: int
    ) -> DataFrame:
        output = df
        (
            output[f"MACD {fastperiod} {slowperiod} {signalperiod}"],
            output[f"MACD signal {fastperiod} {slowperiod} {signalperiod}"],
            output[f" MACD hist {fastperiod} {slowperiod} {signalperiod}"],
        ) = talib.MACD(
            df["Close"],
            fastperiod=fastperiod,
            slowperiod=slowperiod,
            signalperiod=signalperiod,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MACDEXT(
        df: DataFrame,
        fastperiod: int,
        fastmatype: int,
        slowperiod: int,
        slowmatype: int,
        signalperiod: int,
        signalmatype: int,
    ) -> DataFrame:
        output = df
        (
            output[f"MACDEXT_macd {fastperiod} {slowperiod} {signalperiod}"],
            output[f"MACDEXT_macdsignal {fastperiod} {slowperiod} {signalperiod}"],
            output[f"MACDEXT_macdhist {fastperiod} {slowperiod} {signalperiod}"],
        ) = talib.MACDEXT(
            df["Close"],
            fastperiod=fastperiod,
            fastmatype=fastmatype,
            slowperiod=slowperiod,
            slowmatype=slowmatype,
            signalperiod=signalperiod,
            signalmatype=signalmatype,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MACDFIX(df: DataFrame, signalperiod: int) -> DataFrame:
        output = df
        (
            output[f"MACDEXT_macd {signalperiod}"],
            output[f"MACDEXT_macdsignal {signalperiod}"],
            output[f"MACDEXT_macdhist {signalperiod}"],
        ) = talib.MACDFIX(df["Close"], signalperiod=signalperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MFI(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        df[f"MFI {timeperiod}"] = talib.MFI(
            df["High"], df["Low"], df["Close"], df["Volume"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MINUS_DI(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MINUS_DI {timeperiod}"] = talib.MINUS_DI(
            df["High"], df["Low"], df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MINUS_DM(df: DataFrame, timeperiod) -> DataFrame:
        output = df
        output[f"MINUS_DM {timeperiod}"] = talib.MINUS_DM(
            df["High"], df["Low"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def MOM(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"MOM {timeperiod}"] = talib.MOM(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def PLUS_DI(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"PLUS_DI {timeperiod}"] = talib.PLUS_DI(
            df["High"], df["Low"], df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def PLUS_DM(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"PLUS_DM {timeperiod}"] = talib.PLUS_DM(
            df["High"], df["Low"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def PPO(df: DataFrame, fastperiod: int, slowperiod: int, matype: int) -> DataFrame:
        output = df
        output[f"PPO {fastperiod} {slowperiod}"] = talib.PPO(
            df["Close"], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ROC(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"ROC {timeperiod}"] = talib.ROC(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ROCP(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"ROCP {timeperiod}"] = talib.ROCP(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ROCR(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"ROCR {timeperiod}"] = talib.ROCR(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ROCR100(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"ROCR100 {timeperiod}"] = talib.ROCR100(
            df["Close"], timeperiod=timeperiod
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def RSI(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"RSI {timeperiod}"] = talib.RSI(df["Close"], timeperiod=timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def STOCH(
        df: DataFrame,
        fastk_period,
        slowk_period,
        slowk_matype,
        slowd_period,
        slowd_matype,
    ) -> DataFrame:
        output = df
        (
            output[f"STOCH_slowk {fastk_period} {slowk_period} {slowd_period}"],
            output[f"STOCH_slowd {fastk_period} {slowk_period} {slowd_period}"],
        ) = talib.STOCH(
            df["High"],
            df["Low"],
            df["Close"],
            fastk_period=fastk_period,
            slowk_period=slowk_period,
            slowd_period=slowd_period,
            slowk_matype=slowk_matype,
            slowd_matype=slowd_matype,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def STOCHF(df: DataFrame, fastk_period: int, fastd_period: int, fastd_matype: int) -> DataFrame:
        output = df
        (
            output[f"STOCHF_fastk {fastk_period} {fastd_period}"],
            output[f"STOCHF_fastd {fastk_period} {fastd_period}"],
        ) = talib.STOCHF(
            df["High"],
            df["Low"],
            df["Close"],
            fastk_period=fastk_period,
            fastd_period=fastd_period,
            fastd_matype=fastd_matype,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def STOCHRSI(df: DataFrame, timeperiod, fastk_period, fastd_period, fastd_matype) -> DataFrame:
        output = df
        (
            output[f"STOCHRSI_fastk {timeperiod} {fastk_period} {fastd_period}"],
            output[f"STOCHRSI_fastk {timeperiod} {fastk_period} {fastd_period}"],
        ) = talib.STOCHRSI(
            df["Close"],
            timeperiod=timeperiod,
            fastk_period=fastk_period,
            fastd_period=fastd_period,
            fastd_matype=fastd_matype,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def TRIX(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"TRIX {timeperiod}"] = talib.TRIX(df["Close"], timeperiod)
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def ULTOSC(df: DataFrame, timeperiod1: int, timeperiod2: int, timeperiod3: int) -> DataFrame:
        output = df
        output[f"ULTOSC {timeperiod1} {timeperiod2} {timeperiod3}"] = talib.ULTOSC(
            df["High"],
            df["Low"],
            df["Close"],
            timeperiod1=timeperiod1,
            timeperiod2=timeperiod2,
            timeperiod3=timeperiod3,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def WILLR(df: DataFrame, timeperiod: int) -> DataFrame:
        output = df
        output[f"WILLR {timeperiod}"] = talib.WILLR(
            df["High"], df["Low"], df["Close"], timeperiod=timeperiod
        )
        return output
