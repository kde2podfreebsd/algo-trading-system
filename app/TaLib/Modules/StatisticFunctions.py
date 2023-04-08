from app.TaLib.TAInterface import TAInterface


class StatisticFunctions(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def BETA():
        pass

    @staticmethod
    def CORREL():
        pass

    @staticmethod
    def LINEARREG():
        pass

    @staticmethod
    def LINEARREG_ANGLE():
        pass

    @staticmethod
    def LINEARREG_INTERCEPT():
        pass

    @staticmethod
    def LINEARREG_SLOPE():
        pass

    @staticmethod
    def STDDEV():
        pass

    @staticmethod
    def TSF():
        pass

    @staticmethod
    def VAR():
        pass
