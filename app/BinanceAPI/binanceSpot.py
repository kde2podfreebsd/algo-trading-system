from app.SingletonWrapper import singleton
from app.Logger import Logger
from binance.spot import Spot
from binance.error import ClientError, ServerError, ParameterRequiredError, \
    ParameterValueError, ParameterTypeError, ParameterArgumentError
import pandas as pd
from typing import Optional, List, NoReturn, Union, Mapping, Text, Tuple, Sequence
from pandas import DataFrame

log = Logger()


@singleton
class BinanceSpot:
    def __init__(self) -> NoReturn:
        self.client = Spot()
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        log.logger.info("Init Binance Spot not auth Client")

    def get_spot_tickers(self) -> List[str] | Exception:
        try:
            log.logger.info()
            return list(map(lambda x: x.get('symbol'), self.client.ticker_price()))
        except ClientError or ServerError or ParameterTypeError or ParameterArgumentError or ParameterValueError or ParameterRequiredError as err:
            log.logger.error(f"Binance API Error: [{err}]")
            raise err
        except Exception as err:
            log.logger.error(f"Error: [{err}]")

    def get_ticker_price(self, ticker: str | List[str]) -> Union[
        Mapping[Text, Optional[Text]],
        Tuple[Tuple[Text, Optional[Text]], ...],
        Sequence[Tuple[Text, Optional[Text]]],
    ]:
        try:
            if isinstance(ticker, list):
                output = self.client.ticker_price(symbols=ticker)
                log.logger.info(output)
                return output
            if isinstance(ticker, str):
                output = self.client.ticker_price(symbol=ticker)
                log.logger.info(output)
                return output
        except ClientError or ServerError or ParameterTypeError or ParameterArgumentError or ParameterValueError or ParameterRequiredError as err:
            log.logger.error(f"Binance API Error: [{err}]")
            raise err
        except Exception as err:
            log.logger.error(f"Error: [{err}]")

    def get_ticker_24h(self, ticker: str | List[str]) -> Tuple[Tuple[Text, Optional[Text]], ...]:
        try:
            if isinstance(ticker, str):
                return self.client.ticker_24hr(ticker, symbols=None, type="FULL")
            if isinstance(ticker, str):
                return self.client.ticker_24hr(symbol=None, symbols=ticker, type="FULL")
        except ClientError or ServerError or ParameterTypeError or ParameterArgumentError or ParameterValueError or ParameterRequiredError as err:
            log.logger.error(f"Binance API Error: [{err}]")
            raise err
        except Exception as err:
            log.logger.error(f"Error: [{err}]")


    def klines(self):
        r = self.client.klines("BTCUSDT", "1h", limit=300)
        df = DataFrame(r).iloc[:, :5]
        df.columns = list("tohlc")
        df['ma_fast'] = df['c'].ewm(span=12, adjust=False).mean()
        df['ma_slow'] = df['c'].ewm(span=26, adjust=False).mean()
        print(df.tail(10))


b = BinanceSpot()
# b.klines()
# b.get_spot_tickers()
# print(b.get_ticker_price(ticker=["BTCUSDT", "ETHUSDT"]))
# print(b.get_ticker_price(ticker="BTCUSDT"))
b.get_ticker_24h(ticker=None, type_of_request=None)