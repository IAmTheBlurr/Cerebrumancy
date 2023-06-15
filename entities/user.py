""" User class """
from .role import Role


class User(Role):
    """ User entity """
    def __init__(self, message: str, name: str = ""):
        super().__init__(message, name)
        self.role = "user"
