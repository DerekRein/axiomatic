from .Core.Enums import Side
from decimal import Decimal
from .Contract import Contract
from typing import List
from .Fill import Fill


class Order(object):
    """
    Represent an order, either filled or unfilled.
    """

    def __init__(self, contract: Contract, amount: Decimal, side: Side):
        super(Order, self).__init__()

        self._side = side
        self._amount = amount
        self._contract = contract
        self._fills: List[Fill] = []

    def filled(self) -> bool:
        """
        Returns true if the amount has been fulfilled
        :return:
        """
        return sum([f.quantity for f in self._fills]) >= self._amount

    def __iadd__(self, other: Fill):
        """
        :param other: fill object
        :return:
        """
        self._fills.append(other)
        return True

