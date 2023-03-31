from app.SingletonWrapper import singleton
from binance.spot import Spot


@singleton
class BinanceAPI:
    def __init__(self):
        self.client = Spot()
        print(self.client.time())

# b = BinanceAPI()