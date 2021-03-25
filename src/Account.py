from typing import Optional
from decimal import Decimal


class Account(object):
    """
    Describes an account
    """

    def __init__(self, base_currency="USD"):

        self._baseCurrency: Optional[str] = base_currency
        self._cash = Decimal(10000)
