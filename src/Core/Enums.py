from enum import IntEnum

__all__ = ["AssetCategories", "Side"]


class AssetCategories(IntEnum):

    Equity = 1
    Forex = 2
    Crypto = 3


class Side(IntEnum):

    BUY = 0
    SELL = 1


class OrderType(IntEnum):
    Limit = 0
    Market = 1

