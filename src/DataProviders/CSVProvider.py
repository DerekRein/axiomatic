from ._base import BaseDataProvider
from os import path


class CsvProvider(BaseDataProvider):

    def __init__(self, file: path):
        super(CsvProvider, self).__init__()

        self._path = file
