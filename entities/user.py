""" User class """
from .role import Role


class User(Role):
    """ User entity """
    def __init__(self, name: str):
        super().__init__(name=name)
        self.joined_chat = None
        self.memory = []
        self.role = 'user'

    def __call__(self, *args, **kwargs):
        if isinstance(args[0], str):
            self.content = args[0]

        self.memory.append(self.message_data)
        return self

    def join(self, chat):
        """ Join a chat """
        self.joined_chat = chat

    def say(self, message: str):
        """ Say something """
        if not self.joined_chat:
            raise ValueError('User must be joined to a chat before saying something.')

        self.content = message
        self.memory.append(self.message_data)

        response = self.joined_chat.prompt(self)
        self.memory.append(response.message_data)
