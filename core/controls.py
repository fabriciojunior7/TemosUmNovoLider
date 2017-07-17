import pygame

scheme = dict()
state = dict()


def handle():
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            state[event.key] = pygame.time.get_ticks()

        if event.type == pygame.KEYUP:
            del state[event.key]


def register_key(name, key):
    scheme[name] = key


def get_key(name):
    key = scheme.get(name, None)

    if key in state:
        return pygame.time.get_ticks() - state[key]
