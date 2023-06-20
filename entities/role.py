""" Role entity """


class Role(object):
    """ Role entity """
    def __init__(self, name: str):
        self.name = name
        self.content = ''
        self.__role = 'role'

    def __call__(self, *args, **kwargs):
        if isinstance(args[0], str):
            self.content = args[0]

        return self

    def __dict__(self):
        payload = {
            "role": self.__role,
            "content": self.content
        }

        if self.name:
            payload["name"] = self.name

        return payload

    @property
    def role(self):
        """ Return the role """
        return self.__role

    @role.setter
    def role(self, role: str):
        """ Set the role """
        self.__role = role

    @property
    def data(self):
        """ Return the data payload as a dictionary """
        return self.__dict__()
