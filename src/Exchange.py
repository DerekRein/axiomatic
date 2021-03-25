from datetime import time, datetime
from typing import Optional


class Exchange(object):

    def __init__(self):
        self._open: Optional[time] = None
        self._close: Optional[time] = None
        self._open_ext: Optional[time] = None
        self._close_ext: Optional[time] = None

    def isOpen(self):
        return datetime.now().time() < self._close

