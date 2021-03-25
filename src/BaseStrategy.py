from .Account import Account
from .Core.Primitives import Bar, Tick
from typing import Union
from .Session import Session


class AbstractStrategy(object):
    """
    Would be better to have this be graphical...
    """

    def __init__(self):
        self._active_trades = []
        self._complete_trades = []
        self.account = Account()
        self.session = Session()

    def initialize(self):
        pass

    def data(self, data: Union[Bar, Tick]):
        """
        Pass data into here like a table model
        :param data:
        :return:
        """
        pass
