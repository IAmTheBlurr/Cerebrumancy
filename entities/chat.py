""" Chat entity """
from typing import List, Optional, Union

from configuration import Configuration
from .assistant import Assistant
from .system import System
from .user import User
from .chat_response import ChatResponse

import openai


class Chat(object):
    """ Chat entity """
    def __init__(self, config: Configuration, messages: Optional[List] = None, model: str = 'gpt-3.5-turbo'):
        self.model = model
        self.messages = []
        self.__config = config
        self.__openai = openai
        self.__openai.api_key = self.__config.openai_api_key
        self.__temperature = 0

        if messages:
            self.add_messages(messages)

    def add_message(self, role: Union[Assistant, System, User]):
        """ Add a message to the chat message stack """
        self.messages.append(role.message_data)

    def add_messages(self, participants: List[Union[Assistant, System, User]]):
        """ Add messages to the chat message stack """
        for participant in participants:
            if isinstance(participant, User):
                if participant.joined_chat != self and participant.joined_chat is not None:
                    raise ValueError('User is already joined to a different chat')
                participant.join(self)

            self.add_message(participant)

    def add_system(self, system: System):
        """ Add a system to the chat """
        # Check to see if the system is already in the chat
        for index, message in enumerate(self.messages):
            if message['role'] == 'system':
                self.messages.pop(index)
                break

        self.messages.append(system.message_data)

    def get_models(self):
        """ Get the models """
        models = self.__openai.Model.list()
        return [model.id for model in models.data]

    def prompt(self, user: Union[Assistant, System, User]) -> ChatResponse:
        """ Say something """
        self.messages.append(user.message_data)

        response = ChatResponse(openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=self.__temperature,
        ))

        self.messages.append(response.message_data)

        return response
