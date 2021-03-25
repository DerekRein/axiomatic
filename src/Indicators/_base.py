from decimal import Decimal
from typing import Optional


class BaseIndicator(object):

    """
    Has to be provide current and past values
    """

    def __init__(self):
        super(BaseIndicator, self).__init__()
        self._warm = False  # if there is enough data for a real value

    def value(self, n=0) -> Optional[Decimal]:
        """
        The currenct value of the indicator
        :return:
        """
        if not self._warm:
            return None
        return Decimal(10)


class PrimaryIndicator(object):

    """
    Moving averages and such
    """

    def __init__(self):
        super(PrimaryIndicator, self).__init__()


class SecondaryIndicator(object):

    """
    Oscilators
    """

    def __init__(self):
        super(SecondaryIndicator, self).__init__()


class BarIndicator(object):

    """
    Non-continuous events, DOJI etc
    """

    def __init__(self):
        super(BarIndicator, self).__init__()
