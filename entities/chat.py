""" Chat entity """
from typing import List

from configuration import Configuration

import openai


class Chat(object):
    """ Chat entity """
    def __init__(self, config: Configuration, messages: List, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.__messages = messages
        self.__config = config
        self.__openai = openai
        self.__openai.api_key = self.__config.openai_api_key
        self.__temperature = 0

    def create(self):
        """ Create a chat completion """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=self.__temperature,
        )

        print(response["choices"][0]["message"]["content"])

    @property
    def messages(self):
        """ Return the messages as a list """
        return [message.data() for message in self.__messages]
