from TaLib.TAInterface import TAInterface


class CycleIndicators(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def HT_DCPERIOD():
        pass

    @staticmethod
    def HT_DCPHASE():
        pass

    @staticmethod
    def HT_PHASOR():
        pass

    @staticmethod
    def HT_SINE():
        pass

    @staticmethod
    def HT_TRENDMODE():
        pass
