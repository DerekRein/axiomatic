from ._base import PrimaryIndicator
from talib import EMA as ta_EMA
import numpy as np


class EMA(PrimaryIndicator):
    """
    Todo, need to setup some pub/sub to stay subscribed to the current data
    todo, or some react hook types setup where by state can be accessed globally
    these indicators need only provide current and past values
    """

    def __init__(self):
        super(EMA, self).__init__()

    def value(self):
        array = np.array([])
        return ta_EMA(array, 12)
