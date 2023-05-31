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

from Exceptions.BinanceSpotWalletException import BinanceSpotWalletException
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
class BinanceSpotWallet(BinanceInterface):
    def __init__(self, base_url: Optional[str] = "https://testnet.binance.vision"):
        # self.__apiKey = config["Binance"]["apiKey"]
        # self.__apiSecret = config["Binance"]["apiSecret"]
        self.__apiKey = config['Binance']['apiKey']
        self.__apiSecret = config['Binance']['apiSecret']
        self.__client = Spot(
            api_key=self.__apiKey, api_secret=self.__apiSecret, base_url=base_url
        )

    def system_status(self):
        try:
            output = self.__client.system_status()
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def coin_info(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.coin_info(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def account_snapshot(
            self,
            type: str,
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
    ):
        """
        type (str): -- mandatory/string -- "SPOT", "MARGIN", "FUTURES"
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')
            elif type != 'SPOT' and type != 'MARGIN' and type != 'FUTURES':
                raise BinanceSpotWalletException(err='"type" can only be: SPOT or MARGIN or FUTURES')

            output = self.__client.account_snapshot(
                type=type,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def disable_fast_withdraw(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.disable_fast_withdraw(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def enable_fast_withdraw(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.enable_fast_withdraw(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def withdraw(
            self,
            coin: str,
            amount: float,
            address: str,
            withdrawOrderId: Optional[str],
            network: Optional[str],
            addressTag: Optional[str],
            name: Optional[str],
            recvWindow: Optional[int],
            walletType: Optional[int] = 0,
            transactionFeeFlag: Optional[bool] = 'False',
    ):
        """
        withdrawOrderId (str, optional): Client id for withdraw
        addressTag (str, optional): Secondary address identifier for coins like XRP,XMR etc.
        transactionFeeFlag (bool, optional): When making internal transfer,
                                             'True' for returning the fee to the destination account;
                                             'False' for returning the fee back to the departure account.
                                             Default: 'False'.
        name (str, optional): Description of the address. Space in name should be encoded into %20.
        walletType (int, optional): The wallet type for withdraw，0-spot wallet，1-funding wallet. Default is spot wallet
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')
            elif walletType != 0 and walletType != 1:
                raise BinanceSpotWalletException(err='"walletType" can only be: 0 -> spot wallet; 1 -> funding wallet ')
            elif transactionFeeFlag != 'True' and transactionFeeFlag != 'False':
                raise BinanceSpotWalletException(err='"transactionFeeFlag" can only be: "True" or "False"')

            output = self.__client.withdraw(
                coin=coin,
                amount=amount,
                address=address,
                withdrawOrderId=withdrawOrderId,
                network=network,
                addressTag=addressTag,
                name=name,
                recvWindow=recvWindow,
                walletType=walletType,
                transactionFeeFlag=transactionFeeFlag,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def deposit_history(
            self,
            coin: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            status: Optional[int] = 0,
            offset: Optional[int] = 0,
            limit: Optional[int] = 1000,
    ):
        """
        status (int, optional): Default 0 (0:pending, 6: credited but cannot withdraw, 1:success)
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        offset (int, optional): Default value: 0
        limit (int, optional): Default:1000, Max:1000
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')
            elif status != 0 and status != 6 and status != 1:
                raise BinanceSpotWalletException(
                    err='"status" can only be: 0 -> pending; 6 -> credited, by cannot withdraw; 1 -> success')
            elif limit > 1000:
                raise BinanceSpotWalletException(err='"limit" over max limit 1000')

            output = self.__client.deposit_history(
                coin=coin,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                status=status,
                offset=offset,
                limit=limit,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def withdraw_history(
            self,
            coin: Optional[str],
            withdrawOrderId: Optional[str],
            offset: Optional[int],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            status: Optional[int] = 0,
            limit: Optional[int] = 1000,
    ):
        """
        status (int, optional): Default 0 (0: Email Sent, 1: Cancelled, 2: Awaiting Approval,
                3: Rejected, 4: Processing, 5: Failure, 6: Completed)
        startTime (int, optional): Default: 90 days from current timestamp
        endTime (int, optional): Default: present timestamp
        limit (int, optional): Default:1000, Max:1000
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')
            elif status != 0 and status != 1 and status != 2 and status != 3 and status != 4 and status != 5 and status != 6:
                raise BinanceSpotWalletException(
                    err='"status" can only be: 0-Email Sent, 1-Cancelled, 2-Awaiting Approval, 3-Rejected, 4-Processing, 5-Failure, 6-Completed)')
            elif limit > 1000:
                raise BinanceSpotWalletException(err='"limit" over max limit 1000')

            output = self.__client.withdraw_history(
                coin=coin,
                withdrawOrderId=withdrawOrderId,
                offset=offset,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                status=status,
                limit=limit,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def deposit_address(
            self,
            coin: Optional[str],
            network: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.deposit_address(
                coin=coin,
                network=network,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def account_status(self, recvWindow: Optional[str]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.account_status(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def api_trading_status(self, recvWindow: Optional[str]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.api_trading_status(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def dust_log(self, recvWindow: Optional[str]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.dust_log(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def user_universal_transfer(
            self,
            type: str,
            asset: str,
            amount: str,
            fromSymbol: Optional[str],
            toSymbol: Optional[str],
            recvWindow: Optional[str],
    ):
        """
        fromSymbol (str, optional): Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        toSymbol (str, optional): Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.user_universal_transfer(
                type=type,
                asset=asset,
                amount=amount,
                fromSymbol=fromSymbol,
                toSymbol=toSymbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def user_universal_transfer_history(
            self,
            type: str,
            startTime: Optional[int],
            endTime: Optional[int],
            fromSymbol: Optional[str],
            toSymbol: Optional[str],
            recvWindow: Optional[str],
            current: Optional[int] = 1,
            size: Optional[int] = 10,
    ):
        """
        fromSymbol (str, optional): Must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        toSymbol (str, optional): Must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Default 1
        size (int, optional): Default 10, Max 100
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')
            elif size > 100:
                raise BinanceSpotWalletException(err='"size" value over max limit 100')

            output = self.__client.user_universal_transfer_history(
                type=type,
                startTime=startTime,
                endTime=endTime,
                fromSymbol=fromSymbol,
                toSymbol=toSymbol,
                recvWindow=recvWindow,
                current=current,
                size=size,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def transfer_dust(
            self,
            asset: str,
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.transfer_dust(
                asset=asset,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def asset_dividend_record(
            self,
            asset: Optional[str],
            startTime: Optional[int],
            endTime: Optional[int],
            recvWindow: Optional[int],
            limit: Optional[int] = 20,
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        limit (int, optional): Default 20, max 500
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" is over limit 60000')
            elif limit > 500:
                raise BinanceSpotWalletException(err='"limit" value is over max limit 500')

            output = self.__client.asset_dividend_record(
                asset=asset,
                startTime=startTime,
                endTime=endTime,
                recvWindow=recvWindow,
                limit=limit,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def asset_detail(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" is over limit 60000')

            output = self.__client.asset_detail(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def trade_fee(
            self,
            symbol: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" is over limit 60000')

            output = self.__client.trade_fee(
                symbol=symbol,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def funding_wallet(
            self,
            asset: Optional[str],
            needBtcValuation: Optional[str],
            recvWindow: Optional[int]
    ):
        """
        needBtcValuation (str, optional): true or false
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" is over limit 60000')
            elif needBtcValuation != 'true' and needBtcValuation != 'false':
                raise BinanceSpotWalletException(err='"needBtcValuation" can only be: "true" or "false"')

            output = self.__client.funding_wallet(
                asset=asset,
                needBtcValuation=needBtcValuation,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def user_asset(
            self,
            asset: Optional[str],
            needBtcValuation: Optional[str],
            recvWindow: Optional[int]
    ):
        """
        asset (str, optional): If asset is blank, then query all positive assets user have
        needBtcValuation (str, optional): true or false
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" is over limit 60000')
            elif needBtcValuation != 'true' and needBtcValuation != 'false':
                raise BinanceSpotWalletException(err='"needBtcValuation" can only be: "true" or "false"')

            output = self.__client.user_asset(
                asset=asset,
                needBtcValuation=needBtcValuation,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def api_key_permissions(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" is over limit 60000')

            output = self.__client.api_key_permissions(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def bnb_convertible_assets(self, recvWindow: Optional[int]):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" is over limit 60000')

            output = self.__client.bnb_convertible_assets(recvWindow=recvWindow)
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def convertible_coins(self):
        try:
            output = self.__client.convertible_coins()
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def toggle_auto_convertion(
            self,
            coin: str,
            enable: bool,
    ):
        try:
            output = self.__client.toggle_auto_convertion(
                coin=coin,
                enable=enable,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def cloud_mining_trans_history(
            self,
            startTime: int,
            endTime: int,
            tranId: Optional[int],
            clientTranId: Optional[str],
            asset: Optional[str],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[int] = 100,
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Default Value: 1
        size (int, optional): Default Value: 100; Max Value: 100
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')
            elif size > 100:
                raise BinanceSpotWalletException(err='"size" value over max limit 100')

            output = self.__client.cloud_mining_trans_history(
                startTime=startTime,
                endTime=endTime,
                tranId=tranId,
                clientTranId=clientTranId,
                asset=asset,
                recvWindow=recvWindow,
                current=current,
                size=size,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def convert_transfer(
            self,
            clientTranId: str,
            asset: str,
            amount: float,
            targetAsset: str,
            accountType: Optional[str],
            recvWindow: Optional[int],
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')

            output = self.__client.convert_transfer(
                clientTranId=clientTranId,
                asset=asset,
                amount=amount,
                targetAsset=targetAsset,
                accountType=accountType,
                recvWindow=recvWindow,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)

    def convert_history(
            self,
            startTime: int,
            endTime: int,
            tranId: Optional[int],
            clientTranId: Optional[str],
            asset: Optional[str],
            recvWindow: Optional[int],
            current: Optional[int] = 1,
            size: Optional[int] = 100,
    ):
        """
        recvWindow (int, optional): The value cannot be greater than 60000
        current (int, optional): Default Value: 1
        size (int, optional): Default Value: 100; Max Value: 100
        """
        try:
            if recvWindow > 60000:
                raise BinanceSpotWalletException(err='"recvWindow" over limit 60000')
            elif size > 100:
                raise BinanceSpotWalletException(err='"size" value over max limit 100')

            output = self.__client.convert_history(
                startTime=startTime,
                endTime=endTime,
                tranId=tranId,
                clientTranId=clientTranId,
                asset=asset,
                recvWindow=recvWindow,
                current=current,
                size=size,
            )
            logging.debug(output)
            return output

        except Exception:
            raise BinanceSpotWalletException(err=Exception)
