"""Pygame display"""
import signal
from multiprocessing.connection import Connection

import pygame

#: Black RGB value
BLACK = (0, 0, 0)
#: White RGB value
WHITE = (255, 255, 255)

#: Screen size
SIZE = (640, 640)


def display(conn: Connection):
    """Display Game of Life using pygame

    Parameters
    ----------
    conn: Connection
        Multiprocess pipe mainly used for receiving game of life states.

        The first value read from the pipe is the frame delay. Subsequent reads
        yield the game state. When the simulation is over, the display function
        will receive a ``SIGTERM`` signal indicating it should terminate.

        If the display function is terminated early (e.g. by a user closing the
        pygame window), the display function is expected to write a ``SIGTERM``
        signal into the pipe before terminating. This will stop the simulation
        process as well.

    Returns
    -------
    ``SIGTERM``
    """
    pygame.init()

    # Moving the mouse slows down pygame
    pygame.event.set_blocked(pygame.MOUSEMOTION)

    screen = pygame.display.set_mode(SIZE)
    scale = 6
    pygame.display.set_caption("PyGoL - Conway's Game of Life")

    running = True
    clock = pygame.time.Clock()

    delay = conn.recv()
    fps = 1/delay

    while running:
        screen.fill(WHITE)
        world = conn.recv()

        if world == signal.SIGTERM:
            running = False
            break

        for y in range(world.height):
            for x in range(world.width):
                if world[y][x] == 1:
                    # screen.set_at((x, y), BLACK)
                    pygame.draw.rect(
                        screen, BLACK, ((x*scale, y*scale), (scale, scale)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(fps)

    pygame.quit()
    conn.send(signal.SIGTERM)
    conn.close()
    return signal.SIGTERM
