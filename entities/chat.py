""" Chat entity """
from typing import List, Optional

from configuration import Configuration
from .user import User
from .chat_response import ChatResponse

import openai


class Chat(object):
    """ Chat entity """
    def __init__(self, config: Configuration, messages: Optional[List] = None, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.messages = messages
        self.__config = config
        self.__openai = openai
        self.__openai.api_key = self.__config.openai_api_key
        self.__temperature = 0

    def create(self, messages: List):
        """ Create a chat completion """
        self.messages = messages
        return self

    def say(self, message: str):
        """ Say something """
        self.messages.append(User(message))

        response = ChatResponse(openai.ChatCompletion.create(
            model=self.model,
            messages=[message.data for message in self.messages],
            temperature=self.__temperature,
        ))

        self.messages.append(response.message())
