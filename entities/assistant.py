""" Assistant entity """
from .role import Role


class Assistant(Role):
    """ Assistant entity """
    def __init__(self, message: str, name: str = ""):
        super().__init__(message, name)
        self.role = "assistant"
