""" User class """
from .role import Role


class User(Role):
    """ User entity """
    def __init__(self, name: str):
        super().__init__(name=name)
        self.role = 'user'
