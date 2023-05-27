from abc import ABC

import talib
from pandas.core.frame import DataFrame

from TaLib.TAInterface import TAInterface


class PatternRecognition(TAInterface, ABC):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL2CROWS(df: DataFrame):
        output = df
        output["CDL2CROWS"] = talib.CDL2CROWS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL3BLACKCROWS(df: DataFrame):
        output = df
        output["CDL3BLACKCROWS"] = talib.CDL3BLACKCROWS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL3INSIDE(df: DataFrame):
        output = df
        output["CDL3INSIDE"] = talib.CDL3INSIDE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL3LINESTRIKE(df: DataFrame):
        output = df
        output["CDL3LINESTRIKE"] = talib.CDL3LINESTRIKE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL3OUTSIDE(df: DataFrame):
        output = df
        output["CDL3OUTSIDE"] = talib.CDL3OUTSIDE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL3STARSINSOUTH(df: DataFrame):
        output = df
        output["CDL3STARSINSOUTH"] = talib.CDL3STARSINSOUTH(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL3WHITESOLDIERS(df: DataFrame):
        output = df
        output["CDL3WHITESOLDIERS"] = talib.CDL3WHITESOLDIERS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLABANDONEDBABY(df: DataFrame, penetration: float):
        output = df
        output["CDLABANDONEDBABY"] = talib.CDLABANDONEDBABY(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            penetration=penetration,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLADVANCEBLOCK(df: DataFrame):
        output = df
        output["CDLADVANCEBLOCK"] = talib.CDLADVANCEBLOCK(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLBELTHOLD(df: DataFrame):
        output = df
        output["CDLBELTHOLD"] = talib.CDLBELTHOLD(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLBREAKAWAY(df: DataFrame):
        output = df
        output["CDLBREAKAWAY"] = talib.CDLBREAKAWAY(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLCLOSINGMARUBOZU(df: DataFrame):
        output = df
        output["CDLCLOSINGMARUBOZU"] = talib.CDLCLOSINGMARUBOZU(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLCONCEALBABYSWALL(df: DataFrame):
        output = df
        output["CDLCONCEALBABYSWALL"] = talib.CDLCONCEALBABYSWALL(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLCOUNTERATTACK(df: DataFrame):
        output = df
        output["CDLCOUNTERATTACK"] = talib.CDLCOUNTERATTACK(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLDARKCLOUDCOVER(df: DataFrame, penetration: float):
        output = df
        output["CDLDARKCLOUDCOVER"] = talib.CDLDARKCLOUDCOVER(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            penetration=penetration,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLDOJI(df: DataFrame):
        output = df
        output["CDLDOJI"] = talib.CDLDOJI(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLDOJISTAR(df: DataFrame):
        output = df
        output["CDLDOJISTAR"] = talib.CDLDOJISTAR(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLDRAGONFLYDOJI(df: DataFrame):
        output = df
        output["CDLDRAGONFLYDOJI"] = talib.CDLDRAGONFLYDOJI(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLENGULFING(df: DataFrame):
        output = df
        output["CDLENGULFING"] = talib.CDLENGULFING(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLEVENINGDOJISTAR(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLEVENINGSTAR(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLGAPSIDESIDEWHITE(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLGRAVESTONEDOJI(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHAMMER(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHANGINGMAN(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHARAMI(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHARAMICROSS(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHIGHWAVE(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHIKKAKE(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHIKKAKEMOD(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHOMINGPIGEON(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLIDENTICAL3CROWS(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLINNECK(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLINVERTEDHAMMER(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLKICKING(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLKICKINGBYLENGTH(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLLADDERBOTTOM(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLLONGLEGGEDDOJI(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLLONGLINE(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMARUBOZU(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMATCHINGLOW(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMATHOLD(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMORNINGDOJISTAR(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMORNINGSTAR(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLONNECK(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLPIERCING(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLRICKSHAWMAN(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLRISEFALL3METHODS(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSEPARATINGLINES(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSHOOTINGSTAR(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSHORTLINE(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSPINNINGTOP():
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSTALLEDPATTERN(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSTICKSANDWICH(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTAKURI(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTASUKIGAP(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTHRUSTING(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTRISTAR(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLUNIQUE3RIVER(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLUPSIDEGAP2CROWS(df: DataFrame):
        pass

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLXSIDEGAP3METHODS(df: DataFrame):
        pass
