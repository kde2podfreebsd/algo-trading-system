from app.SingletonWrapper import singleton
from binance import Client
from binance.exceptions import BinanceAPIException

@singleton
class BinanceAPI:
    def __init__(self):
        pass