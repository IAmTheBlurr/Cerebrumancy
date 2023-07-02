import os


class FileHandler(object):
    def __init__(self, filename: str):
        self.filename = filename

    @property
    def exists(self):
        return os.path.exists(self.filename)

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def write(self, content: str):
        with open(self.filename, 'w') as f:
            f.write(content)
