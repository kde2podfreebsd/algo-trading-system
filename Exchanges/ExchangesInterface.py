import datetime
from abc import ABCMeta
from abc import abstractmethod
from typing import Any
from typing import List
from typing import Optional
from typing import Union

from pandas import DataFrame

# from abc import abstractstaticmethod
# import pandas as pd

# from abc import abstractclassmethod


class ExchangesInterface(object):
    apiKeys: list[str] | None
    __metaclass__ = ABCMeta

    @property
    def modules(self):
        return self.__function_groups.keys()

    @property
    def exchangeName(self):
        return self._exchangeName

    @exchangeName.setter
    def exchangeName(self, value):
        self._exchangeName = value

    @abstractmethod
    def __init__(self, apiKeys: Optional[List[str]]):
        self.apiKeys = apiKeys

    __function_groups = {"key": ["value"]}

    @abstractmethod
    def makeTimePeriodDataFrame(
        self,
        startTIme: Union[str | datetime.datetime] = None,
        endTime: Union[str | datetime.datetime] = None,
        bar_interval: Any = None,
        symbol: str = None,
    ) -> DataFrame:
        """ """
        return DataFrame
