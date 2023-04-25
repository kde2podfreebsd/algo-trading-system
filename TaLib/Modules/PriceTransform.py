from TaLib.TAInterface import TAInterface


class PriceTransform(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def AVGPRICE():
        pass

    @staticmethod
    def MEDPRICE():
        pass

    @staticmethod
    def TYPPRICE():
        pass

    @staticmethod
    def WCLPRICE():
        pass
