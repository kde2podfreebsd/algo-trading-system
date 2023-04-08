from app.TaLib.TAInterface import TAInterface


class VolumeIndicators(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def AD():
        pass

    @staticmethod
    def ADOSC():
        pass

    @staticmethod
    def OBV():
        pass
