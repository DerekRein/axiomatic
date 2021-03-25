from .Contract import Contract
from datetime import datetime
from typing import Optional
from __future__ import annotations
from decimal import Decimal


class Fill(object):
    """
    A fill on a trade
    """
    def __init__(self, price: Decimal, quantity: Decimal, contract: Contract, time: Optional[datetime] = None):
        super(Fill, self).__init__()

        self.time = datetime.now() if not time else time
        self.price = price
        self.quantity = quantity  # quantity should be negative for sells
        self.contract = contract

    def __gt__(self, other: Fill) -> bool:
        return other.price > self.price
