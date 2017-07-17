import os
import json


class Settings(object):

    def __init__(self, path, defaults=None):
        self.path = path
        self.defaults = defaults or dict()
        self.data = dict()
        self.reset()

    def reset(self):
        try:
            with open(self.path, 'r') as f:
                self.data = json.load(f)
        except IOError:
            return

    def commit(self):
        with open(self.path, 'w') as f:
            json.dump(dict(self.defaults, **self.data), f, indent=2)

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        try:
            return self.data[key]
        except KeyError:
            return self.defaults[key]
