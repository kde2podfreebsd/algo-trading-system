from pandas.core.frame import DataFrame

import talib
from TaLib.TAInterface import TAInterface


class PatternRecognition(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDL2CROWS(df: DataFrame) -> DataFrame:
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
    def CDL3BLACKCROWS(df: DataFrame) -> DataFrame:
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
    def CDL3INSIDE(df: DataFrame) -> DataFrame:
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
    def CDL3LINESTRIKE(df: DataFrame) -> DataFrame:
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
    def CDL3OUTSIDE(df: DataFrame) -> DataFrame:
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
    def CDL3STARSINSOUTH(df: DataFrame) -> DataFrame:
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
    def CDL3WHITESOLDIERS(df: DataFrame) -> DataFrame:
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
    def CDLABANDONEDBABY(df: DataFrame, penetration: float) -> DataFrame:
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
    def CDLADVANCEBLOCK(df: DataFrame) -> DataFrame:
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
    def CDLBELTHOLD(df: DataFrame) -> DataFrame:
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
    def CDLBREAKAWAY(df: DataFrame) -> DataFrame:
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
    def CDLCLOSINGMARUBOZU(df: DataFrame) -> DataFrame:
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
    def CDLCONCEALBABYSWALL(df: DataFrame) -> DataFrame:
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
    def CDLCOUNTERATTACK(df: DataFrame) -> DataFrame:
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
    def CDLDARKCLOUDCOVER(df: DataFrame, penetration: float) -> DataFrame:
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
    def CDLDOJI(df: DataFrame) -> DataFrame:
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
    def CDLDOJISTAR(df: DataFrame) -> DataFrame:
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
    def CDLDRAGONFLYDOJI(df: DataFrame) -> DataFrame:
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
    def CDLENGULFING(df: DataFrame) -> DataFrame:
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
    def CDLEVENINGDOJISTAR(df: DataFrame, penetration: float) -> DataFrame:
        output = df
        output["CDLEVENINGDOJISTAR"] = talib.CDLEVENINGDOJISTAR(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            penetration=penetration,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLEVENINGSTAR(df: DataFrame, penetration: float) -> DataFrame:
        output = df
        output["CDLEVENINGSTAR"] = talib.CDLEVENINGSTAR(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            penetration=penetration,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLGAPSIDESIDEWHITE(df: DataFrame) -> DataFrame:
        output = df
        output["CDLGAPSIDESIDEWHITE"] = talib.CDLGAPSIDESIDEWHITE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLGRAVESTONEDOJI(df: DataFrame) -> DataFrame:
        output = df
        output["CDLGRAVESTONEDOJI"] = talib.CDLGRAVESTONEDOJI(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHAMMER(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHAMMER"] = talib.CDLHAMMER(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHANGINGMAN(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHANGINGMAN"] = talib.CDLHANGINGMAN(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHARAMI(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHARAMI"] = talib.CDLHARAMI(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHARAMICROSS(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHARAMICROSS"] = talib.CDLHARAMICROSS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHIGHWAVE(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHIGHWAVE"] = talib.CDLHIGHWAVE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHIKKAKE(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHIKKAKE"] = talib.CDLHIKKAKE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHIKKAKEMOD(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHIKKAKEMOD"] = talib.CDLHIKKAKEMOD(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLHOMINGPIGEON(df: DataFrame) -> DataFrame:
        output = df
        output["CDLHOMINGPIGEON"] = talib.CDLHOMINGPIGEON(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLIDENTICAL3CROWS(df: DataFrame) -> DataFrame:
        output = df
        output["CDLIDENTICAL3CROWS"] = talib.CDLIDENTICAL3CROWS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLINNECK(df: DataFrame) -> DataFrame:
        output = df
        output["CDLINNECK"] = talib.CDLINNECK(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLINVERTEDHAMMER(df: DataFrame) -> DataFrame:
        output = df
        output["CDLINVERTEDHAMMER"] = talib.CDLINVERTEDHAMMER(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLKICKING(df: DataFrame) -> DataFrame:
        output = df
        output["CDLKICKING"] = talib.CDLKICKING(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLKICKINGBYLENGTH(df: DataFrame) -> DataFrame:
        output = df
        output["CDLKICKINGBYLENGTH"] = talib.CDLKICKINGBYLENGTH(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLLADDERBOTTOM(df: DataFrame) -> DataFrame:
        output = df
        output["CDLLADDERBOTTOM"] = talib.CDLLADDERBOTTOM(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLLONGLEGGEDDOJI(df: DataFrame) -> DataFrame:
        output = df
        output["CDLLONGLEGGEDDOJI"] = talib.CDLLONGLEGGEDDOJI(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLLONGLINE(df: DataFrame) -> DataFrame:
        output = df
        output["CDLLONGLINE"] = talib.CDLLONGLINE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMARUBOZU(df: DataFrame) -> DataFrame:
        output = df
        output["CDLMARUBOZU"] = talib.CDLMARUBOZU(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMATCHINGLOW(df: DataFrame) -> DataFrame:
        output = df
        output["CDLMATCHINGLOW"] = talib.CDLMATCHINGLOW(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMATHOLD(df: DataFrame, penetration: float) -> DataFrame:
        output = df
        output["CDLMATHOLD"] = talib.CDLMATHOLD(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            penetration=penetration,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMORNINGDOJISTAR(df: DataFrame, penetration: float) -> DataFrame:
        output = df
        output["CDLMORNINGDOJISTAR"] = talib.CDLMORNINGDOJISTAR(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            penetration=penetration,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLMORNINGSTAR(df: DataFrame, penetration: float) -> DataFrame:
        output = df
        output["CDLMORNINGSTAR"] = talib.CDLMORNINGSTAR(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            penetration=penetration,
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLONNECK(df: DataFrame) -> DataFrame:
        output = df
        output["CDLONNECK"] = talib.CDLONNECK(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLPIERCING(df: DataFrame) -> DataFrame:
        output = df
        output["CDLPIERCING"] = talib.CDLPIERCING(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLRICKSHAWMAN(df: DataFrame) -> DataFrame:
        output = df
        output["CDLRICKSHAWMAN"] = talib.CDLRICKSHAWMAN(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLRISEFALL3METHODS(df: DataFrame) -> DataFrame:
        output = df
        output["CDLRISEFALL3METHODS"] = talib.CDLRISEFALL3METHODS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSEPARATINGLINES(df: DataFrame) -> DataFrame:
        output = df
        output["CDLSEPARATINGLINES"] = talib.CDLSEPARATINGLINES(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSHOOTINGSTAR(df: DataFrame) -> DataFrame:
        output = df
        output["CDLSHOOTINGSTAR"] = talib.CDLSHOOTINGSTAR(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSHORTLINE(df: DataFrame) -> DataFrame:
        output = df
        output["CDLSHORTLINE"] = talib.CDLSHORTLINE(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSPINNINGTOP(df: DataFrame) -> DataFrame:
        output = df
        output["CDLSPINNINGTOP"] = talib.CDLSPINNINGTOP(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSTALLEDPATTERN(df: DataFrame) -> DataFrame:
        output = df
        output["CDLSTALLEDPATTERN"] = talib.CDLSTALLEDPATTERN(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLSTICKSANDWICH(df: DataFrame) -> DataFrame:
        output = df
        output["CDLSTICKSANDWICH"] = talib.CDLSTICKSANDWICH(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTAKURI(df: DataFrame) -> DataFrame:
        output = df
        output["CDLTAKURI"] = talib.CDLTAKURI(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTASUKIGAP(df: DataFrame) -> DataFrame:
        output = df
        output["CDLTASUKIGAP"] = talib.CDLTASUKIGAP(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTHRUSTING(df: DataFrame) -> DataFrame:
        output = df
        output["CDLTHRUSTING"] = talib.CDLTHRUSTING(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLTRISTAR(df: DataFrame) -> DataFrame:
        output = df
        output["CDLTRISTAR"] = talib.CDLTRISTAR(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLUNIQUE3RIVER(df: DataFrame) -> DataFrame:
        output = df
        output["CDLUNIQUE3RIVER"] = talib.CDLUNIQUE3RIVER(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLUPSIDEGAP2CROWS(df: DataFrame) -> DataFrame:
        output = df
        output["CDLUPSIDEGAP2CROWS"] = talib.CDLUPSIDEGAP2CROWS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output

    @staticmethod
    @TAInterface.is_valid_dataframe
    def CDLXSIDEGAP3METHODS(df: DataFrame) -> DataFrame:
        output = df
        output["CDLXSIDEGAP3METHODS"] = talib.CDLXSIDEGAP3METHODS(
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
        )
        return output
