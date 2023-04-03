from app.TaLib.TABase import TAInterface


class MathOperators(TAInterface):

    def __init__(self, max_rows: int, max_columns: int, width: int):
        super().__init__(max_rows=max_rows, max_columns=max_columns, width=width)

    @staticmethod
    def ADD():
        pass

    @staticmethod
    def DIV():
        pass

    @staticmethod
    def MAX():
        pass

    @staticmethod
    def MAXINDEX():
        pass

    @staticmethod
    def MIN():
        pass

    @staticmethod
    def MININDEX():
        pass

    @staticmethod
    def MINMAX():
        pass

    @staticmethod
    def MINMAXINDEX():
        pass

    @staticmethod
    def MULT():
        pass

    @staticmethod
    def SUB():
        pass

    @staticmethod
    def SUM():
        pass

