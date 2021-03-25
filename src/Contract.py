from .Exchange import Exchange
from .Core.Enums import AssetCategories
from decimal import Decimal


class Contract(object):
    """
    Describes a trading instrument
    """

    def __init__(self, symbol: str, exchange: Exchange, asset_class: AssetCategories):

        self.symbol = symbol
        self.exchange = exchange
        self.asset_class = asset_class
        self.tick_value = Decimal(0.01)

    def __str__(self):
        return self.symbol
