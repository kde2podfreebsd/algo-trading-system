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

    def margin_pair_index(self, symbol: str):
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
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
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

    def margin_load_record(
            self,
            asset: str,
            isolatedSymbol: Optional[str],
            txId: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[int] = 100,
            archived: Optional[str] = 'false',
    ):
        """
        txId (int, optional): the tranId in POST /sapi/v1/margin/loan
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif current < 1:
                raise BinanceSpotMarginException(err='current value starts from 1')
            elif size > 100:
                raise BinanceSpotMarginException(err='size over limit 100')
            elif archived != 'true' and archived != 'false':
                raise BinanceSpotMarginException(err='archived can only be: true or false')

            output = self.__client.margin_load_record(
                asset=asset,
                isolatedSymbol=isolatedSymbol,
                txId=txId,
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

    def margin_repay_record(
            self,
            asset: str,
            isolatedSymbol: Optional[str],
            txId: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[int] = 100,
            archived: Optional[str] = 'false',

    ):
        """
        txId (int, optional): the tranId in POST /sapi/v1/margin/loan
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif current < 1:
                raise BinanceSpotMarginException(err='current value starts from 1')
            elif size > 100:
                raise BinanceSpotMarginException(err='size over limit 100')
            elif archived != 'true' and archived != 'false':
                raise BinanceSpotMarginException(err='archived can only be: true or false')

            output = self.__client.margin_repay_record(
                asset=asset,
                isolatedSymbol=isolatedSymbol,
                txId=txId,
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

    def margin_interest_history(
            self,
            asset: Optional[str],
            isolatedSymbol: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[int] = 100,
            archived: Optional[str] = 'false',

    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif current < 1:
                raise BinanceSpotMarginException(err='current value starts from 1')
            elif size > 100:
                raise BinanceSpotMarginException(err='size over limit 100')
            elif archived != 'true' and archived != 'false':
                raise BinanceSpotMarginException(err='archived can only be: true or false')

            output = self.__client.margin_interest_history(
                asset=asset,
                isolatedSymbol=isolatedSymbol,
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

    def margin_force_liquidation_record(
            self,
            isolatedSymbol: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[int] = 100,
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif current < 1:
                raise BinanceSpotMarginException(err='current value starts from 1')
            elif size > 100:
                raise BinanceSpotMarginException(err='size over limit 100')

            output = self.__client.margin_force_liquidation_record(
                isolatedSymbol=isolatedSymbol,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                current=current,
                size=size,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_order(
            self,
            symbol: str,
            orderId: Optional[str],
            origClientOrderId: Optional[str],
            recvWindow: Optional[int],
            isIsolated: Optional[str] = 'FALSE',
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')

            output = self.__client.margin_order(
                symbol=symbol,
                orderId=orderId,
                origClientOrderId=origClientOrderId,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_open_orders_cancellation(
            self,
            symbol: str,
            recvWindow: Optional[int],
            isIsolated: Optional[str] = 'FALSE',
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')

            output = self.__client.margin_open_orders_cancellation(
                symbol=symbol,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_all_orders(
            self,
            symbol: str,
            orderId: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            isIsolated: Optional[str] = 'FALSE',
            limit: Optional[int] = 500,
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE"
        limit (int, optional): Default 500; max 500.
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')
            if limit > 500:
                raise BinanceSpotMarginException(err='limit maximum value: 500')

            output = self.__client.margin_all_orders(
                symbol=symbol,
                orderId=orderId,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
                limit=limit,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_my_trades(
            self,
            symbol: str,
            fromID: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            isIsolated: Optional[str] = 'FALSE',
            limit: Optional[int] = 500,
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE"
        limit (int, optional): Default 500; max 500.
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')
            if limit > 500:
                raise BinanceSpotMarginException(err='limit maximum value: 500')

            output = self.__client.margin_my_trades(
                symbol=symbol,
                fromID=fromID,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
                limit=limit,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_max_borrowable(
            self,
            asset: str,
            isolatedSymbol: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_max_borrowable(
                asset=asset,
                isolatedSymbol=isolatedSymbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_max_transferable(
            self,
            asset: str,
            isolatedSymbol: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_max_transferable(
                asset=asset,
                isolatedSymbol=isolatedSymbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_transfer(
            self,
            asset: str,
            symbol: str,
            amount: float,
            transFrom: str,
            transTo: str,
            recvWindow: Optional[int],
    ):
        """
        transFrom (str) and transTo (str) can only be: "SPOT" or "ISOLATED_MARGIN"
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if transFrom != "SPOT" and transFrom != "ISOLATED_MARGIN":
                raise BinanceSpotMarginException(err='transFrom can only be: "SPOT" or "ISOLATED_MARGIN"')
            elif transTo != "SPOT" and transTo != "ISOLATED_MARGIN":
                raise BinanceSpotMarginException(err='transTo can only be: "SPOT" or "ISOLATED_MARGIN"')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.isolated_margin_transfer(
                asset=asset,
                symbol=symbol,
                amount=amount,
                transFrom=transFrom,
                transTo=transTo,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_transfer_history(
            self,
            symbol: str,
            asset: Optional[str],
            transFrom: Optional[str],
            transTo: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[itn] = 10,
    ):
        """
        transFrom (str) and transTo (str) can only be: "SPOT" or "ISOLATED_MARGIN"
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        """
        try:
            if transFrom != "SPOT" and transFrom != "ISOLATED_MARGIN":
                raise BinanceSpotMarginException(err='transFrom can only be: "SPOT" or "ISOLATED_MARGIN"')
            elif transTo != "SPOT" and transTo != "ISOLATED_MARGIN":
                raise BinanceSpotMarginException(err='transTo can only be: "SPOT" or "ISOLATED_MARGIN"')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif current < 1:
                raise BinanceSpotMarginException(err='current value starts from 1')
            elif size > 100:
                raise BinanceSpotMarginException(err='size over limit 100')

            output = self.__client.isolated_margin_transfer_history(
                symbol=symbol,
                asset=asset,
                transFrom=transFrom,
                transTo=transTo,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                current=current,
                size=size,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_account(
            self,
            symbols: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        symbols (str, optional): Max 5 symbols can be sent; separated by ",". e.g. "BTCUSDT,BNBUSDT,ADAUSDT"
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if len(symbols.split(",")) > 5:
                raise BinanceSpotMarginException(err='maximum 5 symbols can be sent; separated by ","')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.isolated_margin_account(
                symbols=symbols,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_pair(
            self,
            symbol: str,
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.isolated_margin_pair(
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_all_pairs(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.isolated_margin_all_pairs(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def toggle_bnbBurn(
            self,
            spotBNBBurn: Optional[str],
            interestBNBBurn: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        spotBNBBurn (str, optional): "true" or "false"; Determines whether to use BNB to pay for trading fees on SPOT
        interestBNBBurn (str, optional): "true" or "false"; Determines whether to use BNB to pay for margin loan's interest
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if spotBNBBurn != "true" and spotBNBBurn != "false":
                raise BinanceSpotMarginException(err='spotBNBBurn value can only be: "true" or "false"')
            elif interestBNBBurn != "true" and interestBNBBurn != "false":
                raise BinanceSpotMarginException(err='spotBNBBurn value can only be: "true" or "false"')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.toggle_bnbBurn(
                spotBNBBurn=spotBNBBurn,
                interestBNBBurn=interestBNBBurn,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def bnbBurn_status(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.bnbBurn_status(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_interest_rate_history(
            self,
            asset: str,
            vipLevel: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
    ):
        """
        vipLevel (str, optional): Default: user's vip level
        startTime (int, optional): Default: 7 days ago.
        endTime (int, optional): Default: present. Maximum range: 1 month.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_interest_rate_history(
                asset=asset,
                vipLevel=vipLevel,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def new_margin_oco_order(
            self,
            symbol: str,
            side: str,
            quantity: float,
            price: float,
            stopPrice: float,
            listClientOrderId: Optional[str],
            limitClientOrderId: Optional[str],
            limitIcebergQty: Optional[float],
            stopClientOrderId: Optional[str],
            stopLimitPrice: Optional[float],
            stopIcebergQty: Optional[float],
            stopLimitTimeInForce: Optional[str],
            newOrderRespType: Optional[str],
            recvWindow: Optional[int],
            isIsolated: Optional[str] = 'FALSE',
            sideEffectType: Optional[str] = 'NO_SIDE_EFFECT',
    ):
        """
        listClientOrderId (str, optional): A unique Id for the entire orderList
        limitClientOrderId (str, optional): A unique Id for the limit order
        stopClientOrderId (str, optional): A unique Id for the stop loss/stop loss limit leg
        stopLimitPrice (float, optional): If provided, stopLimitTimeInForce is required
        stopLimitTimeInForce (str, optional): Valid values are GTC/FOK/IOC
        newOrderRespType (str, optional): Set the response JSON
        recvWindow (int, optional): The value cannot be greater than 60000
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        sideEffectType (str, optional): NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY; default NO_SIDE_EFFECT
        """
        try:
            if side != 'BUY' and side != 'SELL':
                raise BinanceSpotMarginException(err='side value can only be: BUY or SELL')
            elif stopLimitTimeInForce != 'GTC' and stopLimitTimeInForce != 'IOC' and stopLimitTimeInForce != 'FOK':
                raise BinanceSpotMarginException(err='timeInForce value can only be: GTC or IOC or FOK')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')
            elif sideEffectType != 'NO_SIDE_EFFECT' and sideEffectType != 'MARGIN_BUY' and sideEffectType != 'AUTO_REPAY':
                raise BinanceSpotMarginException(err='sideEffectType value can only be: NO_SIDE_EFFECT or MARGIN_BUY or AUTO_REPAY')

            output = self.__client.new_margin_oco_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
                stopPrice=stopPrice,
                listClientOrderId=listClientOrderId,
                limitClientOrderId=limitClientOrderId,
                limitIcebergQty=limitIcebergQty,
                stopClientOrderId=stopClientOrderId,
                stopLimitPrice=stopLimitPrice,
                stopIcebergQty=stopIcebergQty,
                stopLimitTimeInForc=stopLimitTimeInForce,
                newOrderRespType=newOrderRespType,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
                sideEffectType=sideEffectType,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def cancel_margin_oco_order(
            self,
            symbol: str,
            newClientOrderId: Optional[str],
            recvWindow: Optional[int],
            orderListId: int = None,
            listClientOrderId: str = None,
            isIsolated: Optional[str] = 'FALSE'
    ):
        """
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        listClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        newClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default.
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.cancel_margin_oco_order(
                symbol=symbol,
                orderListId=orderListId,
                listClientOrderId=listClientOrderId,
                isIsolated=isIsolated,
                newClientOrderId=newClientOrderId,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def get_margin_oco_order(
            self,
            symbol: Optional[str],
            recvWindow: Optional[int],
            orderListId: int = None,
            origClientOrderId: str = None,
            isIsolated: Optional[str] = 'FALSE'

    ):
        """
        orderListId (int, optional): Either orderListId or origClientOrderId must be provided
        origClientOrderId (str, optional): Either orderListId or origClientOrderId must be provided.
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        symbol (str, optional): Mandatory for isolated margin, not supported for cross margin
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.get_margin_oco_order(
                orderListId=orderListId,
                origClientOrderId=origClientOrderId,
                isIsolated=isIsolated,
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def get_margin_oco_orders(
            self,
            symbol: Optional[str],
            fromID: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            isIsolated: Optional[str] = 'FALSE',
            limit: Optional[int] = 500,
    ):
        """
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        symbol (str, optional): Mandatory for isolated margin, not supported for cross margin
        fromId (int, optional): If supplied, neither startTime nor endTime can be provided
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')
            elif limit > 1000:
                raise BinanceSpotMarginException(err='limit maximum value: 1000')

            output = self.__client.get_margin_oco_orders(
                symbol=symbol,
                fromID=fromID,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
                limit=limit,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def cancel_isolated_margin_account(
            self,
            symbol: str,
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.cancel_isolated_margin_account(
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def enable_isolated_margin_account(
            self,
            symbol: str,
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.enable_isolated_margin_account(
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_account_limit(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.isolated_margin_account_limit(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_fee(
            self,
            vipLevel: Optional[int],
            coin: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        vipLevel (int, optional): User's current specific margin data will be returned if vipLevel is omitted
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_fee(
                vipLevel=vipLevel,
                coin=coin,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_fee(
            self,
            vipLevel: Optional[int],
            symbol: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        vipLevel (int, optional): User's current specific margin data will be returned if vipLevel is omitted
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.isolated_margin_fee(
                vipLevel=vipLevel,
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def isolated_margin_tier(
            self,
            symbol: str,
            tier: Optional[int],
            recvWindow: Optional[int],
    ):
        """
        tier (int, optional): All margin tier data will be returned if tier is omitted
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.isolated_margin_tier(
                symbol=symbol,
                tier=tier,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_order_usage(
            self,
            symbol: Optional[str],
            recvWindow: Optional[int],
            isIsolated: Optional[str] = 'FALSE',
    ):
        """
        isIsolated (str, optional): for isolated margin or not, "TRUE", "FALSE", default "FALSE"
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if isIsolated != 'FALSE' and isIsolated != 'TRUE':
                raise BinanceSpotMarginException(err='isIsolated value can only be: TRUE or FALSE')
            elif recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_order_usage(
                symbol=symbol,
                recvWindow=recvWindow,
                isIsolated=isIsolated,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def margin_dust_log(
            self,
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
    ):
        """
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.margin_dust_log(
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)

    def summary_of_margin_account(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotMarginException(err='recvWindow over limit 60000')

            output = self.__client.summary_of_margin_account(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotMarginException(err=Exception)
