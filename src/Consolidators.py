from typing import List
from .Core.Primitives import Bar, Tick


class BarConsolidator(object):

    """
    Consolidates bars into a higher time frame
    """

    def __init__(self):
        super(BarConsolidator, self).__init__()
        self._bars: List[Bar] = []

    def __iadd__(self, other: Bar):
        self._bars.append(other)


class TickConsolidator(object):

    """
    Consolidates ticks into bars
    """

    def __init__(self):
        super(TickConsolidator, self).__init__()
        self._ticks: List[Tick] = []

    def __iadd__(self, other: Tick):
        self._ticks.append(other)

