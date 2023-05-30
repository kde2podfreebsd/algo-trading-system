import configparser
import logging

from binance.error import ClientError
from binance.lib.utils import config_logging
from binance.um_futures import UMFutures

from settings import basedir
from settings import setup_logger

# from datetime import datetime
# from datetime import timezone
# from typing import Any
# from typing import Dict
from typing import List
from typing import Optional

# from typing import Sequence
# from typing import Union
# from pandas import DataFrame
# from Exceptions import BinanceSpotMarketException
# from Exchanges.Binance.BinanceInterface import BinanceInterface


config = configparser.ConfigParser()
config.read(f"{basedir}/config.ini")

logger = logging.getLogger(__name__)


# setup_logger(logger=logger)


class UMFuturesClient(object):
    __instance = None

    def __init__(self):
        if not UMFuturesClient.__instance:
            self.__apiKey = config["Binance_Futures"]["apiKey"]
            self.__apiSecret = config["Binance_Futures"]["apiSecret"]

            config_logging(logging, logging.DEBUG)

            self.um_futures_client = UMFutures(self.__apiKey, self.__apiSecret)
            self.um_futures_client.base_url = "https://testnet.binancefuture.com"
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        try:
            if not cls.__instance:
                cls.__instance = UMFuturesClient()
            return cls.__instance
        except Exception as e:
            return e

    def makeOrder(
            self,
            symbol: str,
            side: str,
            orderType: str,
            quantity: float
    ):
        try:
            response = self.um_futures_client.new_order(
                symbol=symbol,
                side=side,
                type=orderType,
                quantity=quantity,
            )
            logging.info(response)
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getAccountTrades(self):
        try:
            response = self.um_futures_client.get_account_trades(
                symbol="BTCUSDT", recvWindow=6000
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def changePositionMode(self, dualSidePosition: str, recvWindow: Optional[int]):
        try:
            response = self.um_futures_client.change_position_mode(
                dualSidePosition=dualSidePosition, recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getPositionMode(self, recvWindow: Optional[int]):
        try:
            response = self.um_futures_client.get_position_mode(recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def changeMultiAssetMode(self, multiAssetsMargin: str, recvWindow: Optional[int]):
        """
        multiAssetsMargin: string; "true": Multi-Assets Mode; "false": Single-Asset Mod
        """
        try:
            response = self.um_futures_client.change_multi_asset_mode(
                multiAssetsMargin=multiAssetsMargin,
                recvWindow=recvWindow
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getMultiAssetMode(self, recvWindow: Optional[int]):
        try:
            response = self.um_futures_client.get_multi_asset_mode(recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def newOrderTest(self, symbol: str, side: str, type: str):
        try:
            response = self.um_futures_client.new_order_test(
                symbol=symbol,
                side=side,
                type=type,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def newBatchOrder(self, symbol: str, side: str, type: str):
        try:
            response = self.um_futures_client.new_batch_order(
                symbol=symbol,
                side=side,
                type=type,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def queryOrder(
            self,
            symbol: str,
            orderId: int = None,
            origClientOrderId: str = None,
    ):
        try:
            response = self.um_futures_client.query_order(
                symbol=symbol,
                orderId=orderId,
                origClientOrderId=origClientOrderId,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def cancelOrder(
            self,
            symbol: str,
            orderId: int = None,
            origClientOrderId: str = None,
    ):
        try:
            response = self.um_futures_client.cancel_order(
                symbol=symbol,
                orderId=orderId,
                origClientOrderId=origClientOrderId,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def cancelOpenOrders(self, symbol: str):
        try:
            response = self.um_futures_client.cancel_open_orders(symbol=symbol)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def cancelBatchOrder(
            self,
            symbol: str,
            orderIdList: list,
            origClientOrderIdList: list
    ):
        try:
            response = self.um_futures_client.cancel_batch_order(
                symbol=symbol,
                orderIdList=orderIdList,
                origClientOrderIdList=origClientOrderIdList,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def countdownCancelOrder(self, symbol: str, countdownTime: int):
        try:
            response = self.um_futures_client.countdown_cancel_order(
                symbol=symbol,
                countdownTime=countdownTime,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getOpenOrders(
            self,
            symbol: str,
            orderId: int = None,
            origClientOrderId: str = None,
    ):
        try:
            response = self.um_futures_client.get_open_orders(
                symbol=symbol,
                orderId=orderId,
                origClientOrderId=origClientOrderId,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getOrders(self):
        try:
            response = self.um_futures_client.get_orders()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getAllOrders(self, symbol: str):
        try:
            response = self.um_futures_client.get_all_orders(symbol=symbol)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def balance(self):
        try:
            response = self.um_futures_client.balance()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def account(self):
        try:
            response = self.um_futures_client.account()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def changeLeverage(self, symbol: str, leverage: int, ):
        try:
            response = self.um_futures_client.change_leverage(
                symbol=symbol,
                leverage=leverage,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def changeMarginType(self, symbol: str, marginType: str):
        try:
            response = self.um_futures_client.change_margin_type(
                symbol=symbol,
                marginType=marginType,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def modifyIsolatedPositionMargin(
            self,
            symbol: str,
            amount: float,
            type: int,
    ):
        try:
            response = self.um_futures_client.modify_isolated_position_margin(
                symbol=symbol,
                amount=amount,
                type=type,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getPositionMarginHistory(self, symbol: str):
        try:
            response = self.um_futures_client.get_position_margin_history(symbol=symbol)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getPositionRisk(self, symbol: str):
        try:
            response = self.um_futures_client.get_position_risk(symbol=symbol)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getIncomeHistory(self):
        try:
            response = self.um_futures_client.get_income_history()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def leverageBrackets(self):
        try:
            response = self.um_futures_client.leverage_brackets()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def adlQuantile(self):
        try:
            response = self.um_futures_client.adl_quantile()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def forceOrders(self):
        try:
            response = self.um_futures_client.force_orders()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def apiTradingStatus(self):
        try:
            response = self.um_futures_client.api_trading_status()
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def commissionRate(self, symbol: str):
        try:
            response = self.um_futures_client.commission_rate(symbol=symbol)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def downloadTransactionsAsyn(
            self,
            startTime: int,
            endTime: int,
    ):
        try:
            response = self.um_futures_client.download_transactions_asyn(
                startTime=startTime,
                endTime=endTime,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def aysncDownloadInfo(self, downloadId: str):
        try:
            response = self.um_futures_client.aysnc_download_info(
                downloadId=downloadId,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )


if __name__ == "__main__":
    umf = UMFuturesClient()
    t = umf.makeOrder(symbol="BTCUSDT", orderType='MARKET', side="BUY", quantity=0.01)
    output = umf.getAccountTrades()
    print(output)
