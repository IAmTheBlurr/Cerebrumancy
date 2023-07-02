""" Chat response entity """
from typing import Dict

from .assistant import Assistant
from .system import System
from .user import User


class ChatResponse:
    """ Chat response entity """
    def __init__(self, data: Dict):
        """
        Chat response entity

        Example data:
            {
              "choices": [
                {
                  "finish_reason": "stop",
                  "index": 0,
                  "message": {
                    "content": "Orange who?",
                    "role": "assistant"
                  }
                }
              ],
              "created": 1679718435,
              "id": "chatcmpl-6xpmlDodtW6RwiaMaC1zhLsR8Y1D3",
              "model": "gpt-3.5-turbo-0301",
              "object": "chat.completion",
              "usage": {
                "completion_tokens": 3,
                "prompt_tokens": 39,
                "total_tokens": 42
              }
            }
        """
        self.content = data["choices"][0]["message"]["content"]
        self.completion_tokens = data["usage"]["completion_tokens"]
        self.data = data
        self.finish_reason = data["choices"][0]["finish_reason"]
        self.index = data["choices"][0]["index"]
        self.model = data["model"]
        self.name = data["name"] if "name" in data else ''
        self.object = data["object"]
        self.prompt_tokens = data["usage"]["prompt_tokens"]
        self.role = data["choices"][0]["message"]["role"]
        self.total_tokens = data["usage"]["total_tokens"]

    @property
    def message_data(self):
        """ Return the message data payload as a dictionary """
        payload = {
            'role': self.role,
            'content': self.content
        }

        if self.name:
            payload['name'] = self.name

        return payload

    def message(self):
        """ Return the message """
        role_map = {
            "assistant": Assistant,
            "system": System,
            "user": User
        }

        if self.name:
            return role_map[self.role](self.content, name=self.name)
        else:
            return role_map[self.role](self.content)
