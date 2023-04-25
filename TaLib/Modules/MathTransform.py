from TaLib.TAInterface import TAInterface


class MathTransform(TAInterface):
    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def ACOS():
        pass

    @staticmethod
    def ASIN():
        pass

    @staticmethod
    def ATAN():
        pass

    @staticmethod
    def CEIL():
        pass

    @staticmethod
    def COS():
        pass

    @staticmethod
    def COSH():
        pass

    @staticmethod
    def EXP():
        pass

    @staticmethod
    def FLOOR():
        pass

    @staticmethod
    def LN():
        pass

    @staticmethod
    def LOG10():
        pass

    @staticmethod
    def SIN():
        pass

    @staticmethod
    def SINH():
        pass

    @staticmethod
    def SQRT():
        pass

    @staticmethod
    def TAN():
        pass

    @staticmethod
    def TANH():
        pass
