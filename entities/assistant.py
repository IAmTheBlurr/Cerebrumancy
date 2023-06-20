""" Assistant entity """
from .role import Role


class Assistant(Role):
    """ Assistant entity """
    def __init__(self, name: str = ''):
        super().__init__(name=name)
        self.role = 'assistant'
