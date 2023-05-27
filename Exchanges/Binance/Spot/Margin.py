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

from Exceptions.BinanceSpotMarginException import BinanceSpotMarginException
from Exchanges.Binance.BinanceInterface import BinanceInterface
from settings import basedir
from settings import setup_logger
from settings import singleton

# from typing import NoReturn

config = configparser.ConfigParser()
config.read(f"{basedir}/config.ini")

logger = logging.getLogger(__name__)
setup_logger(logger=logger)


@singleton
class BinanceSpotMargin(BinanceInterface):
    def __init__(self, base_url: Optional[str] = "https://testnet.binance.vision"):
        # self.__apiKey = config["Binance"]["apiKey"]
        # self.__apiSecret = config["Binance"]["apiSecret"]
        self.__apiKey = config['Binance']['apiKey']
        self.__apiSecret = config['Binance']['apiSecret']
        self.__client = Spot(
            api_key=self.__apiKey, api_secret=self.__apiSecret, base_url=base_url
        )

    def margin_transfer(
        self,
        asset: str,
        amount: float,
        type: int,
        recvWindow: Optional[int] = None,
    ):
        """
        asset (str): Defines the asset being transferred, e.g., BTC.
        amount (float): Defines the amount to be transferred
        type (int): 1: transfer from main account to cross margin account
                    2: transfer from cross margin account to main account
        recvWindow (int, optional): the value cannot be greater than 60000
        """
        try:
            if type != 1 and type != 2:
                raise BinanceSpotMarginException(
                    err='type can only be: 1 (transfer from main account to cross margin account) or 2 (transfer from cross margin account to main account)')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_transfer(
                asset=asset,
                amount=amount,
                type=type,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_borrow(
        self,
        asset: str,
        amount: float,
        symbol: Optional[str],
        recvWindow: Optional[int] = None,
        isIsolated: Optional[str] = 'FALSE',
    ):
        """
        asset (str): Defines the asset being transferred, e.g., BTC.
        amount (float): Defines the amount to be transferred
        symbol (str, optional): isolated symbol
        recvWindow (int, optional): the value cannot be greater than 60000
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE"
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')

            output = self.__client.margin_borrow(
                asset=asset,
                amount=amount,
                symbol=symbol,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_repay(
        self,
        asset: str,
        amount: float,
        symbol: Optional[str],
        recvWindow: Optional[int],
        isIsolated: Optional[str] = 'FALSE',
    ):
        """
        asset (str): Defines the asset being transferred, e.g., BTC.
        amount (float): Defines the amount to be transferred
        symbol (str, optional): isolated symbol
        recvWindow (int, optional): the value cannot be greater than 60000
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE"
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')

            output = self.__client.margin_repay(
                asset=asset,
                amount=amount,
                symbol=symbol,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_asset(self, asset: str):
        try:
            output = self.__client.margin_asset(asset=asset)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_pair(self, symbol: str):
        try:
            output = self.__client.margin_pair(symbol=symbol)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_all_assets(self):
        try:
            output = self.__client.margin_all_assets()
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_all_pairs(self):
        try:
            output = self.__client.margin_all_pairs()
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_pair_index(self,symbol: str):
        try:
            output = self.__client.margin_pair_index(symbol=symbol)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def new_margin_order(
        self,
        symbol: str,
        side: str,
        type: str,
        quantity: Optional[float],
        quoteOrderQty: Optional[float],
        price: Optional[float],
        stopPrice: Optional[float],
        newClientOrderId: Optional[str],
        icebergQty: Optional[float],
        newOrderRespType: Optional[float],
        timeInForce: Optional[str],
        recvWindow: Optional[int],
        sideEffectType: Optional[str] = 'NO_SIDE_EFFECT',
        isIsolated: Optional[str] = 'FALSE',
    ):
        """
        side (str): can only be 'BUY' or 'SELL'
        stopPrice (float, optional): Used with STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT and TAKE_PROFIT_LIMIT orders.
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT or FULL;
                                          MARKET and LIMIT order types default to FULL,
                                          all other orders default to ACK.
        sideEffectType (str, optional): NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; default NO_SIDE_EFFECT.
        recvWindow (int, optional): the value cannot be greater than 60000
        timeInForce (str, optional): GTC,IOC,FOK
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE"
        """
        try:
            if side != 'BUY' and side != 'SELL':
                raise BinanceSpotMarginException(err='side value can only be: BUY or SELL')
            elif sideEffectType != 'NO_SIDE_EFFECT' and sideEffectType != 'MARGIN_BUY' and sideEffectType != 'AUTO_REPAY':
                raise BinanceSpotMarginException(err='sideEffectType value can only be: NO_SIDE_EFFECT or MARGIN_BUY or AUTO_REPAY')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif timeInForce != 'GTC' and timeInForce != 'IOC' and timeInForce != 'FOK':
                raise BinanceSpotMarginException(err='timeInForce value can only be: GTC or IOC or FOK')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')

            output = self.__client.new_margin_order(
                symbol=symbol,
                side=side,
                type=type,
                quantity=quantity,
                quoteOrderQty=quoteOrderQty,
                price=price,
                stopPrice=stopPrice,
                newClientOrderId=newClientOrderId,
                icebergQty=icebergQty,
                newOrderRespType=newOrderRespType,
                timeInForce=timeInForce,
                recvWindow=recvWindow,
                sideEffectType=sideEffectType,
                isIsolated=isIsolated,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def cancel_margin_order(
        self,
        symbol: str,
        orderId: Optional[int],
        origClientOrderId: Optional[str],
        newClientOrderId: Optional[str],
        recvWindow: Optional[int],
        isIsolated: Optional[str] = 'FALSE',
    ):
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')

            output = self.__client.cancel_margin_order(
                symbol=symbol,
                orderId=orderId,
                origClientOrderId=origClientOrderId,
                newClientOrderId=newClientOrderId,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_transfer_history(
            self,
            asset: str,
            type: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[int] = 10,
            archived: Optional[str] = 'false',
    ):
        """
        type (str, optional): Transfer Type: ROLL_IN, ROLL_OUT
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if type != 'ROLL_IN' and type != 'ROLL_OUT':
                raise BinanceSpotMarginException(err='type value only can be: ROLL_IN or ROLL_OUT')
            elif current < 1:
                raise BinanceSpotMarginException(err='current value starts from 1')
            elif archived != 'true' and archived != 'false':
                raise BinanceSpotMarginException(err='archived can only be: true or false')
            elif size > 100:
                raise BinanceSpotMarginException(err='size over limit 100')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_transfer_history(
                asset=asset,
                type=type,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                current=current,
                size=size,
                archived=archived,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)


