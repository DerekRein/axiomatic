
class BaseEvent(object):

    def __init__(self):
        super(BaseEvent, self).__init__()


class OnBarUpdate(BaseEvent):

    def __init__(self):
        super(OnBarUpdate, self).__init__()


class OnOrderUpdate(BaseEvent):

    def __init__(self):
        super(OnOrderUpdate, self).__init__()