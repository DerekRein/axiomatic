
from decimal import Decimal
from typing import Optional, List
from datetime import datetime
from __future__ import annotations


class Bar(object):

    """
    Basic OHLCV bar
    """

    def __init__(self, time: datetime, _open: Decimal, high: Decimal, low: Decimal, close: Decimal, volume: Optional[Decimal]):
        super(Bar, self).__init__()
        self._time = time
        self._open = _open
        self._high = high
        self._low = low
        self._close = close
        self._volume = volume

    def hlc(self):
        return (self._high + self._low + self._close) / 3

    def ohlc(self):
        return (self._open + self._high + self._low + self._close) / 4


class Tick(object):

    """
    Basic Tick Object
    """

    def __init__(self, time: datetime, price: Decimal, volume: Decimal):
        super(Tick, self).__init__()
        self._time = time
        self._price = price
        self._volume = volume

    def __gt__(self, other: Tick):
        pass

    def __lt__(self, other):
        pass

    def __str__(self):
        pass
