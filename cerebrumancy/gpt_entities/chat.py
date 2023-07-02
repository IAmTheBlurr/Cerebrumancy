""" Chat entity """
from typing import List, Optional, Union

from cerebrumancy.core import Config
from .assistant import Assistant
from .system import System
from .user import User

import openai


class Chat(object):
    """ Chat entity """
    def __init__(self, config: Config, messages: Optional[List] = None, model: str = 'gpt-3.5-turbo'):
        self.model = model
        self.messages = []
        self.user_assigned = None
        self.__config = config
        self.__openai = openai
        self.__openai.api_key = self.__config.openai_api_key

        if messages:
            self.add_messages(messages)

    def add_message(self, role: Union[Assistant, System, User]):
        """ Add a message to the chat message stack """
        self.messages.append(role.message_data)

    def add_messages(self, participants: List[Union[Assistant, System, User]]):
        """ Add messages to the chat message stack """
        for participant in participants:
            self.add_message(participant)
