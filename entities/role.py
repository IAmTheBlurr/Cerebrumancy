""" Role entity """


class Role(object):
    """ Role entity """
    def __init__(self, message: str, name: str = ""):
        self.name = name
        self.content = message
        self.__role = "role"

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
