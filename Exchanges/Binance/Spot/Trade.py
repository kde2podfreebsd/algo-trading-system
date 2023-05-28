import configparser
import logging
from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union

from binance.spot import Spot
from pandas import DataFrame

from Exceptions.BinanceSpotTradeException import BinanceSpotTradeException
from Exchanges.Binance.BinanceInterface import BinanceInterface
from settings import basedir
from settings import setup_logger
from settings import singleton

# from datetime import timezone

# from typing import NoReturn

config = configparser.ConfigParser()
config.read(f"{basedir}/config.ini")

logger = logging.getLogger(__name__)
setup_logger(logger=logger)


@singleton
class BinanceSpotTrade(BinanceInterface):
    def __init__(self, base_url: Optional[str] = "https://testnet.binance.vision"):
        # self.__apiKey = config["Binance"]["apiKey"]
        # self.__apiSecret = config["Binance"]["apiSecret"]
        self.__apiKey = config["Binance"]["apiKey"]
        self.__apiSecret = config["Binance"]["apiSecret"]
        self.__client = Spot(
            api_key=self.__apiKey, api_secret=self.__apiSecret, base_url=base_url
        )

    def new_order_test(
            self,
            symbol: str,
            side: str,
            type: str,
            timeInForce: Optional[str],
            quantity: Optional[float],
            quoteOrderQty: Optional[float],
            price: Optional[float],
            newClientOrderId: Optional[str],
            stopPrice: Optional[float],
            icebergQty: Optional[float],
            newOrderRespType: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                                     MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')

            output = self.__client.new_order_test(
                symbol=symbol,
                side=side,
                type=type,
                timeInForce=timeInForce,
                quantity=quantity,
                quoteOrderQty=quoteOrderQty,
                price=price,
                newClientOrderId=newClientOrderId,
                stopPrice=stopPrice,
                icebergQty=icebergQty,
                newOrderRespType=newOrderRespType,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def new_order(
            self,
            symbol: str,
            side: str,
            type: str,
            timeInForce: Optional[str],
            quantity: Optional[float],
            quoteOrderQty: Optional[float],
            price: Optional[float],
            newClientOrderId: Optional[str],
            strategyId: Optional[int],
            strategyType: Optional[int],
            stopPrice: Optional[float],
            icebergQty: Optional[float],
            newOrderRespType: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        strategyType (int, optional): The value cannot be less than 1000000.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT, or FULL;
                                     MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')
            elif strategyType < 1000000:
                raise BinanceSpotTradeException(err='"strategyType" cannot be less then 1000000')

            output = self.__client.new_order(
                symbol=symbol,
                side=side,
                type=type,
                timeInForce=timeInForce,
                quantity=quantity,
                quoteOrderQty=quoteOrderQty,
                price=price,
                newClientOrderId=newClientOrderId,
                strategyId=strategyId,
                strategyType=strategyType,
                stopPrice=stopPrice,
                icebergQty=icebergQty,
                newOrderRespType=newOrderRespType,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def cancel_order(
            self,
            symbol: str,
            orderId: Optional[str],
            origClientOrderId: Optional[str],
            newClientOrderId: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')

            output = self.__client.cancel_order(
                symbol=symbol,
                orderId=orderId,
                origClientOrderId=origClientOrderId,
                newClientOrderId=newClientOrderId,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def cancel_open_orders(
            self,
            symbol: str,
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')

            output = self.__client.cancel_open_orders(
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def get_order(
            self,
            symbol: str,
            orderId: Optional[int],
            origClientOrderId: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')

            output = self.__client.get_order(
                symbol=symbol,
                orderId=orderId,
                origClientOrderId=origClientOrderId,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def cancel_and_replace(
            self,
            symbol: str,
            side: str,
            type: str,
            cancelReplaceMode: str,
            timeInForce: Optional[str],
            quantity: Optional[float],
            quoteOrderQty: Optional[float],
            price: Optional[float],
            cancelNewClientOrderId: Optional[str],
            cancelOrigClientOrderId: Optional[str],
            cancelOrderId: Optional[int],
            newClientOrderId: Optional[str],
            strategyId: Optional[int],
            strategyType: Optional[int],
            stopPrice: Optional[float],
            trailingDelta: Optional[float],
            icebergQty: Optional[float],
            newOrderRespType: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        timeInForce (str, optional): Order time in force
        quantity (float, optional): Order quantity
        quoteOrderQty (float, optional): Quote quantity
        price (float, optional): Order price
        cancelNewClientOrderId (str, optional): Used to uniquely identify this cancel.
                                                Automatically generated by default
        cancelOrigClientOrderId (str, optional): Either the cancelOrigClientOrderId or cancelOrderId must be provided.
                                                If both are provided, cancelOrderId takes precedence.
        cancelOrderId (int, optional): Either the cancelOrigClientOrderId or cancelOrderId must be provided.
                                                If both are provided, cancelOrderId takes precedence.
        newClientOrderId (str, optional): Used to identify the new order. Automatically generated by default
        strategyType (int, optional): The value cannot be less than 1000000.
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        trailingDelta (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. MARKET and LIMIT order types default to FULL,
                                            all other orders default to ACK.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')
            elif strategyType < 1000000:
                raise BinanceSpotTradeException(err='"strategyType" cannot be less then 1000000')

            output = self.__client.cancel_and_replace(
                symbol=symbol,
                side=side,
                type=type,
                cancelReplaceMode=cancelReplaceMode,
                timeInForce=timeInForce,
                quantity=quantity,
                quoteOrderQty=quoteOrderQty,
                price=price,
                cancelNewClientOrderId=cancelNewClientOrderId,
                cancelOrigClientOrderId=cancelOrigClientOrderId,
                cancelOrderId=cancelOrderId,
                newClientOrderId=newClientOrderId,
                strategyId=strategyId,
                strategyType=strategyType,
                stopPrice=stopPrice,
                trailingDelta=trailingDelta,
                icebergQty=icebergQty,
                newOrderRespType=newOrderRespType,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def get_open_orders(
            self,
            symbol: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')

            output = self.__client.get_open_orders(
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def get_orders(
            self,
            symbol: str,
            orderId: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            limit: Optional[int] = 500,
    ):
        """
        limit (int, optional): Default 500; max 1000.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')
            elif limit > 1000:
                raise BinanceSpotTradeException(err='"limit" value is over max limit 1000')

            output = self.__client.get_orders(
                symbol=symbol,
                orderId=orderId,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                limit=limit,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def new_oco_order(
            self,
            symbol: str,
            side: str,
            quantity: float,
            price: float,
            stopPrice: float,
            listClientOrderId: Optional[str],
            limitClientOrderId: Optional[str],
            limitStrategyId: Optional[int],
            limitStrategyType: Optional[int],
            limitIcebergQty: Optional[float],
            stopClientOrderId: Optional[str],
            stopStrategyId: Optional[int],
            stopStrategyType: Optional[int],
            stopLimitPrice: Optional[float],
            stopIcebergQty: Optional[float],
            stopLimitTimeInForce: Optional[str],
            newOrderRespType: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        listClientOrderId (str, optional): A unique Id for the entire orderList
        limitStrategyType (int, optional): The value cannot be less than 1000000.
        stopStrategyType (int, optional): The value cannot be less than 1000000.
        newOrderRespType (str, optional): Set the response JSON.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')
            elif limitStrategyType < 1000000:
                raise BinanceSpotTradeException(err='"limitStrategyType" cannot be less than 1000000')
            elif stopStrategyType < 1000000:
                raise BinanceSpotTradeException(err='"stopStrategyType" cannot be less than 1000000')

            output = self.__client.new_oco_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
                stopPrice=stopPrice,
                listClientOrderId=listClientOrderId,
                limitClientOrderId=limitClientOrderId,
                limitStrategyId=limitStrategyId,
                limitStrategyType=limitStrategyType,
                limitIcebergQty=limitIcebergQty,
                stopClientOrderId=stopClientOrderId,
                stopStrategyId=stopStrategyId,
                stopStrategyType=stopStrategyType,
                stopLimitPrice=stopLimitPrice,
                stopIcebergQty=stopIcebergQty,
                stopLimitTimeInForce=stopLimitTimeInForce,
                newOrderRespType=newOrderRespType,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def cancel_oco_order(
            self,
            symbol: str,
            orderListId: Optional[int],
            listClientOrderId: Optional[str],
            newClientOrderId: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        listClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided
        newClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')

            output = self.__client.cancel_oco_order(
                symbol=symbol,
                orderListId=orderListId,
                listClientOrderId=listClientOrderId,
                newClientOrderId=newClientOrderId,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def get_oco_order(
            self,
            orderListId: Optional[int],
            origClientOrderId: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        origClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')

            output = self.__client.get_oco_order(
                orderListId=orderListId,
                origClientOrderId=origClientOrderId,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def get_oco_orders(
            self,
            fromId: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            limit: Optional[int] = 500,
    ):
        """
        fromId (int, optional): If supplied, neither startTime nor endTime can be provided
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')
            elif limit > 1000:
                raise BinanceSpotTradeException(err='"limit" is over max limit 1000')

            output = self.__client.get_oco_orders(
                fromId=fromId,
                startTime=startTime,
                endTime=endTime,
                limit=limit,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def get_oco_open_orders(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" over limit 60000')

            output = self.__client.get_oco_open_orders(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def account(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" over limit 60000')

            output = self.__client.account(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def my_trades(
            self,
            symbol: str,
            fromId: Optional[int],
            orderId: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            limit: Optional[int] = 500,
    ):
        """
        fromId (int, optional): TradeId to fetch from. Default gets most recent trades.
        orderId (int, optional): This can only be used in combination with symbol
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" is over limit 60000')
            elif limit > 1000:
                raise BinanceSpotTradeException(err='"limit" is over max limit 1000')

            output = self.__client.my_trades(
                symbol=symbol,
                fromId=fromId,
                orderId=orderId,
                startTime=startTime,
                endTime=endTime,
                limit=limit,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)

    def get_order_rate_limit(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotTradeException(err='"recvWindow" over limit 60000')

            output = self.__client.get_order_rate_limit(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotTradeException(err=Exception)
