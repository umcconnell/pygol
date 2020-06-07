"""Terminal display"""
import os
import signal
import time
from multiprocessing.connection import Connection


def display(conn: Connection) -> None:
    """Display Game of Life in the terminal

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
    delay = conn.recv()

    while True:
        os.system("clear")

        world = conn.recv()
        if world == signal.SIGTERM:
            return signal.SIGTERM

        print(world)
        time.sleep(delay)
