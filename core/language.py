import json


class Language(object):

    def __init__(self, path, encoding='utf-8'):
        with open(path, 'r') as f:
            self.data = json.load(f, encoding)

    def translate(self, string):
        return self.data.get(string, string)
