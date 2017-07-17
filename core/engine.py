import pygame
import controls


def run(title, screen, fps=60):
    pygame.init()
    pygame.display.set_caption(title)

    resolution = (1280, 720)
    flags = pygame.DOUBLEBUF & pygame.OPENGL

    display = pygame.display.set_mode(resolution, flags)
    clock = pygame.time.Clock()

    while screen is not None:
        render(screen, display)
        delta = clock.tick(fps)

        if pygame.event.peek(pygame.QUIT):
            break

        controls.handle(delta)
        screen = screen.update(delta)

    pygame.display.quit()


def render(screen, display):
    display.fill(0x000000)
    screen.render(display)
    pygame.display.flip()
