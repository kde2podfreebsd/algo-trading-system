import configparser
import logging

from binance.error import ClientError
from binance.lib.utils import config_logging
from binance.cm_futures import CMFutures

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


class CMFuturesClient(object):
    __instance = None

    def __init__(self):
        if not CMFuturesClient.__instance:
            self.__apiKey = config["Binance_Futures"]["apiKey"]
            self.__apiSecret = config["Binance_Futures"]["apiSecret"]

            config_logging(logging, logging.DEBUG)

            self.cm_futures_client = CMFutures(self.__apiKey, self.__apiSecret)
            self.cm_futures_client.base_url = "https://testnet.binancefuture.com"
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        try:
            if not cls.__instance:
                cls.__instance = CMFuturesClient()
            return cls.__instance
        except Exception as e:
            return e

    def makeOrder(
            self,
            symbol: str,
            side: str,
            type: str,
            quantity: Optional[float],
            positionSide: Optional[str],
            timeInForce: Optional[str],
            reduceOnly: Optional[str],
            price: Optional[float],
            newClientOrderId: Optional[str],
            stopPrice: Optional[float],
            closePosition: Optional[str],
            activationPrice: Optional[float],
            callbackRate: Optional[float],
            recvWindow: Optional[int],
            workingType: Optional[str] = 'CONTRACT_PRICE',
            priceProtect: Optional[str] = 'FALSE',
            newOrderRespType: Optional[float] = 'ACK',
    ):
        """
        positionSide: optional string. Default BOTH for One-way Mode; LONG or SHORT for Hedge Mode. It must be passed in Hedge Mode.
        newClientOrderId: optional string. An unique ID among open orders. Automatically generated if not sent.
        stopPrice: optional float. Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
        closePosition: optional string. true or false; Close-All, use with STOP_MARKET or TAKE_PROFIT_MARKET.
        activationPrice: optional float. Use with TRAILING_STOP_MARKET orders, default is the latest price (supporting different workingType).
        callbackRate: optional float. Use with TRAILING_STOP_MARKET orders, min 0.1, max 5 where 1 for 1%.
        workingType: optional string. stopPrice triggered by: "MARK_PRICE", "CONTRACT_PRICE". Default "CONTRACT_PRICE".
        priceProtect: optional string. "TRUE" or "FALSE", default "FALSE". Use with STOP/STOP_MARKET or TAKE_PROFIT/TAKE_PROFIT_MARKET orders.
        newOrderRespType: optional float. "ACK" or "RESULT", default "ACK".
        """
        try:
            response = self.cm_futures_client.new_order(
                symbol=symbol,
                side=side,
                type=type,
                quantity=quantity,
                positionSide=positionSide,
                timeInForce=timeInForce,
                reduceOnly=reduceOnly,
                price=price,
                newClientOrderId=newClientOrderId,
                stopPrice=stopPrice,
                closePosition=closePosition,
                activationPrice=activationPrice,
                callbackRate=callbackRate,
                workingType=workingType,
                priceProtect=priceProtect,
                newOrderRespType=newOrderRespType,
                recvWindow=recvWindow,
            )
            logging.info(response)
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def modifyOrder(
            self,
            symbol: str,
            side: str,
            quantity: Optional[float],
            price: Optional[float],
            recvWindow: Optional[int],
            orderId: Optional[int] = None,
            origClientOrderId: Optional[str] = None,
    ):
        """
        - Either orderId or origClientOrderId must be sent, and the orderId will prevail if both are sent.
        - Either quantity or price must be sent.
        - If the modification will cause the order to be cancelled immediately, the modification request will be rejected,
            in this case the user can force the modification by sending both quantity and price parameters and let
            the order be cancelled immediately. So if you want to ensure the success of the modification request,
            we strongly recommend sending both quantity and price parameters at the same, for example:
            - When the new order quantity in the modification request is less than the partially filled quantity,
                if the user only sends quantity then the modification will fail, if the user sends both quantity and price then
                the modification will be successful and the order will be cancelled immediately.
            - When the new order price in the modification request prevents the GTX order from becoming a pending
                order (post only), if the user only sends price then the modification will fail, if the user sends both
                quantity and price then the modification will be successful and the order will be cancelled immediately.
        """
        try:
            response = self.cm_futures_client.modify_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
                recvWindow=recvWindow,
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

    def getAccountTrades(
            self,
            symbol: Optional[str],
            pair: Optional[str],
            startTime: Optional[str],
            endTime: Optional[str],
            fromId: Optional[int],
            recvWindow: Optional[int],
            limit: Optional[int] = 50,
    ):
        """
        fromId: optional int; trade ID to fetch from, default is to get the most recent trades.
        limit: optional int; default 50, max 100
        - Either symbol or pair must be sent
        - Symbol and pair cannot be sent together
        - Pair and fromId cannot be sent together
        - If a pair is sent, tickers for all symbols of the pair will be returned
        - The parameter fromId cannot be sent with startTime or endTime
        """
        try:
            response = self.cm_futures_client.get_account_trades(
                symbol=symbol,
                pair=pair,
                startTime=startTime,
                endTime=endTime,
                fromId=fromId,
                recvWindow=recvWindow,
                limit=limit,
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
            response = self.cm_futures_client.change_position_mode(
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
            response = self.cm_futures_client.get_position_mode(recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def newBatchOrder(self, batchOrders: list, recvWindow: Optional[int]):
        """
        - Parameter rules are same with New Order
        - Batch orders are processed concurrently, and the order of matching is not guaranteed.
        - The order of returned contents for batch orders is the same as the order of the order list.
            batchOrders (list): order list. Max 5 orders
        - batchOrders is the list of order parameters in JSON
        """
        try:
            response = self.cm_futures_client.new_batch_order(
                batchOrders=batchOrders,
                recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def modifyBatchOrder(self, batchOrders: list, recvWindow: Optional[int]):
        """
        - Parameter rules are same with New Order
        - Batch orders are processed concurrently, and the order of matching is not guaranteed.
        - The order of returned contents for batch orders is the same as the order of the order list.
            batchOrders (list): order list. Max 5 orders
        - batchOrders is the list of order parameters in JSON
        """
        try:
            response = self.cm_futures_client.modify_batch_order(
                batchOrders=batchOrders,
                recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def orderModifyHistory(
            self,
            symbol: str,
            startTime: Optional[int],
            endTime: Optional[int],
            limit: Optional[int],
            recvWindow: Optional[int],
            orderId: Optional[int] = None,
            origClientOrderId: Optional[str] = None,
    ):
        """
        startTime: optional int; Timestamp in ms to get modification history from INCLUSIVE
        endTime: optional int; Timestamp in ms to get modification history from INCLUSIVE
        """
        try:
            response = self.cm_futures_client.order_modify_history(
                symbol=symbol,
                startTime=startTime,
                endTime=endTime,
                limit=limit,
                recvWindow=recvWindow,
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

    def queryOrder(
            self,
            symbol: str,
            recvWindow: Optional[int],
            orderId: Optional[int] = None,
            origClientOrderId: Optional[str] = None,
    ):
        try:
            response = self.cm_futures_client.query_order(
                symbol=symbol,
                recvWindow=recvWindow,
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
            newClientOrderId: Optional[str],
            recvWindow: Optional[int],
            orderId: Optional[int] = None,
            origClientOrderId: Optional[str] = None,
    ):
        try:
            response = self.cm_futures_client.cancel_order(
                symbol=symbol,
                newClientOrderId=newClientOrderId,
                recvWindow=recvWindow,
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

    def cancelOpenOrders(self, symbol: str, recvWindow: Optional[int]):
        try:
            response = self.cm_futures_client.cancel_open_orders(symbol=symbol, recvWindow=recvWindow)
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
            origClientOrderIdList: list,
            recvWindow: Optional[int],
    ):
        """
        orderIdList: int list, max length 10 e.g. [1234567,2345678]
        origClientOrderIdList: string list, max length 10 e.g. ["my_id_1","my_id_2"], encode the double quotes.
                                No space after comma.
        - Either orderIdList or origClientOrderIdList must be sent.
        """
        try:
            response = self.cm_futures_client.cancel_batch_order(
                symbol=symbol,
                orderIdList=orderIdList,
                origClientOrderIdList=origClientOrderIdList,
                recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def countdownCancelOrder(
            self,
            symbol: str,
            countdownTime: int,
            recvWindow: Optional[int],
    ):
        """
        countdownTime: int list, countdown time, 1000 for 1 second. 0 to cancel the timer
        - The endpoint should be called repeatedly as heartbeats so that the existing countdown time can be canceled
            and replaced by a new one.
        - Example usage:
            - Call this endpoint at 30s intervals with an countdownTime of 120000 (120s).
            - If this endpoint is not called within 120 seconds, all your orders of the specified symbol will be
                automatically canceled.
            - If this endpoint is called with an countdownTime of 0, the countdown timer will be stopped.
        - The system will check all countdowns approximately every 10 milliseconds, so please note that sufficient
            redundancy should be considered when using this function.
        - We do not recommend setting the countdown time to be too precise or too small.
        """
        try:
            response = self.cm_futures_client.countdown_cancel_order(
                symbol=symbol,
                countdownTime=countdownTime,
                recvWindow=recvWindow,
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
            recvWindow: Optional[int],
            orderId: Optional[int] = None,
            origClientOrderId: Optional[str] = None,
    ):
        """
        - Either orderId or origClientOrderId must be sent
        - If the queried order has been filled or cancelled, the error message "Order does not exist" will be returned.
        """
        try:
            response = self.cm_futures_client.get_open_orders(
                symbol=symbol,
                recvWindow=recvWindow,
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

    def getOrders(
            self,
            symbol: Optional[str],
            recvWindow: Optional[int],
    ):
        try:
            response = self.cm_futures_client.get_orders(
                symbol=symbol,
                recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getAllOrders(
            self,
            symbol: str,
            orderId: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            limit: Optional[int] = 50,
    ):
        """
        limit: optional int; default 50, max 100.
        recvWindow: optional int; the value cannot be greater than 60000
        """
        try:
            response = self.cm_futures_client.get_all_orders(
                symbol=symbol,
                orderId=orderId,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                limit=limit,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def balance(self, recvWindow: Optional[int]):
        try:
            response = self.cm_futures_client.balance(recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def account(self, recvWindow: Optional[int]):
        try:
            response = self.cm_futures_client.account(recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def changeLeverage(
            self,
            symbol: str,
            leverage: int,
            recvWindow: Optional[int],
    ):
        """
        leverage: int; target initial leverage: int from 1 to 125
        """
        try:
            response = self.cm_futures_client.change_leverage(
                symbol=symbol,
                leverage=leverage,
                recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def changeMarginType(
            self,
            symbol: str,
            marginType: str,
            leverage: str,
            recvWindow: Optional[int],
    ):
        """
        leverage: string; ISOLATED, CROSSED
        """
        try:
            response = self.cm_futures_client.change_margin_type(
                symbol=symbol,
                marginType=marginType,
                leverage=leverage,
                recvWindow=recvWindow,
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
            positionSide: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        type: int; 1: Add position margin, 2: Reduce position margin
        positionSide: optional string; default BOTH for One-way Mode, LONG or SHORT for Hedge Mode. It must be sent with Hedge Mode.
        """
        try:
            response = self.cm_futures_client.modify_isolated_position_margin(
                symbol=symbol,
                amount=amount,
                type=type,
                positionSide=positionSide,
                recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getPositionMarginHistory(
            self,
            symbol: str,
            type: Optional[int],
            startTime: Optional[str],
            endTime: Optional[str],
            recvWindow: Optional[int],
            limit: Optional[int] = 50,
    ):
        """
        type: optional int; 1: Add position margin，2: Reduce position margin
        limit: optional int; default 50
        """
        try:
            response = self.cm_futures_client.get_position_margin_history(
                symbol=symbol,
                type=type,
                startTime=startTime,
                endTime=endTime,
                limit=limit,
                recvWindow=recvWindow,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getPositionRisk(self, symbol: str, recvWindow: Optional[int]):
        try:
            response = self.cm_futures_client.get_position_risk(symbol=symbol, recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def getIncomeHistory(
            self,
            symbol: Optional[str],
            incomeType: Optional[int],
            startTime: Optional[str],
            endTime: Optional[str],
            recvWindow: Optional[int],
            limit: Optional[int] = 50,
    ):
        """
        incomeType: optional string; "TRANSFER", "WELCOME_BONUS", "REALIZED_PNL", "FUNDING_FEE", "COMMISSION" and "INSURANCE_CLEAR"
        startTime: optional string; timestamp in ms to get funding from INCLUSIVE.
        endTime: optional string; timestamp in ms to get funding from INCLUSIVE.
        limit: optional int; default 50, max 100
        """
        try:
            response = self.cm_futures_client.get_income_history(
                symbol=symbol,
                incomeType=incomeType,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                limit=limit,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def leverageBrackets(
            self,
            recvWindow: Optional[int],
            symbol: Optional[str] = None,
            pair: Optional[str] = None,
    ):
        try:
            response = self.cm_futures_client.leverage_brackets(
                recvWindow=recvWindow,
                symbol=symbol,
                pair=pair,)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def adlQuantile(self, symbol: Optional[str], recvWindow: Optional[int]):
        """
        - Values update every 30s.
        - Values 0, 1, 2, 3, 4 shows the queue position and possibility of ADL from low to high.
        - For positions of the symbol are in One-way Mode or isolated margined in Hedge Mode, "LONG", "SHORT", and "BOTH"
         will be returned to show the positions' adl quantiles of different position sides.
        - If the positions of the symbol are crossed margined in Hedge Mode:
        - "HEDGE" as a sign will be returned instead of "BOTH";
        - A same value calculated on unrealized pnls on long and short sides' positions will be shown for "LONG" and "SHORT"
        when there are positions in both of long and short sides.
        """
        try:
            response = self.cm_futures_client.adl_quantile(symbol=symbol, recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def forceOrders(
            self,
            symbol: Optional[str],
            autoCloseType: Optional[str],
            startTime: Optional[str],
            endTime: Optional[str],
            recvWindow: Optional[int],
            limit: Optional[int] = 50,
    ):
        """
        autoCloseType: optional string; "LIQUIDATION" for liquidation orders, "ADL" for ADL orders.
        limit: optional int; default 50, max 100
        - If "autoCloseType" is not sent, orders with both of the types will be returned
        - If "startTime" is not sent, data within 200 days before "endTime" can be queried
        """
        try:
            response = self.cm_futures_client.force_orders(
                symbol=symbol,
                autoCloseType=autoCloseType,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                limit=limit,
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def commissionRate(self, symbol: str, recvWindow: Optional[int]):
        try:
            response = self.cm_futures_client.commission_rate(symbol=symbol, recvWindow=recvWindow)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
