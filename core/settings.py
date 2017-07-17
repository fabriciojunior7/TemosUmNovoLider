import os
import json


class Settings(object):

    def __init__(self, filename, defaults=None):
        self.filename = filename
        self.defaults = defaults or dict()
        self.data = dict()
        self.reset()

    def reset(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except IOError:
            return

    def commit(self):
        with open(self.filename, 'w') as f:
            json.dump(dict(self.defaults, **self.data), f, indent=2)

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        try:
            return self.data[key]
        except KeyError:
            return self.defaults[key]
