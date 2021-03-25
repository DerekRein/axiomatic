from decimal import Decimal
from typing import Optional, List
from .Fill import Fill
from .Core.Enums import Side


class Trade(object):

    """
    Describes a trade in progress or a completed trade
    """

    def __init__(self):
        self._openingTrade: Optional[bool] = None
        self._fills: List[Fill] = []

    def side(self) -> Side:
        """
        Returns the direction of the trade
        :return: bool
        """
        return Side.BUY if self._fills[0].quantity > 0 else Side.SELL

    def gain(self) -> Decimal:
        return Decimal(100)

    def closed(self) -> bool:
        """
        True if the sum of fill quantity is zero and the number of fills is > 1
        :return:
        """
        if len(self._fills) <= 1:
            return False
        if sum([f.quantity for f in self._fills]) == 0:
            return True

