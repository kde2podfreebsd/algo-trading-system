from TaLib.TAInterface import TAInterface


class VolatilityIndicators(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def ATR():
        pass

    @staticmethod
    def NATR():
        pass

    @staticmethod
    def TRANGE():
        pass
