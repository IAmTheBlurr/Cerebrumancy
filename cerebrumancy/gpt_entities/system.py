""" System entity """
from .role import Role


class System(Role):
    """ System entity """
    def __init__(self, message: str, name: str = ''):
        super().__init__(name)
        self.content = message
        self.role = 'system'
