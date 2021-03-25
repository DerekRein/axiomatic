from datetime import datetime


class Session(object):

    """
    Describes a trading session or backtest
    Event driver
    """

    def __init__(self):
        self.current_time = datetime.now()

    def advance(self, step=1):
        """
        advances the backtest by N
        :param step:
        :return:
        """
        return True
