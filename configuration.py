""" ./configuration.py """
import json
import os


class Configuration(object):
    """ Configuration class for the OpenAI API """
    def __init__(self, file_path: str = ''):
        self.__file_path = ''
        self.openai_api_key = ''

        if file_path:
            self.read_file(file_path)

    @property
    def file_path(self):
        """ The path to the file """
        return self.__file_path

    @file_path.setter
    def file_path(self, value: str):
        if not os.path.isfile(value):
            raise IOError('Value provided as a path to the file does not appear to point to a file.  Please provide a full path to a .json file.')

        self.__file_path = value

    def read_file(self, file_path: str) -> None:
        """ Reads the file and sets the configuration values """
        self.file_path = file_path

        with open(self.file_path) as config:
            data = config.read()

        content = json.loads(data)

        self.openai_api_key = content['openai_api_key'] if 'openai_api_key' in content else ''
