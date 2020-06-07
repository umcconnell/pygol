"""PyGoL Game of Life"""
from __future__ import annotations

import multiprocessing as mp
from signal import SIGTERM
from typing import Any, Callable, List, Union

from pygol.utils import Matrix

from .rules import Signature as Rule
from .rules import conways_life, RULES


class Game(Matrix):
    """PyGoL Game simulation class

    Parameters
    ----------
    width, height: int
        Width and height of the life matrix.

    seed: `list` [`list` [`Any`]], optional
        Seed or base grid to start the simulation with. Must only contain ``0``
        for dead cells and ``1`` for alive cells. When parsing an RLE file this
        seed is returned from ``utils.parse_rle.parse()`` as part of the user
        environment. If not specified, it defaults to a randomly filled matrix.

    wrap: bool, optional
        Whether to wrap the matrix around the edges. Defaults to ``True``.

    rule: `union` [`Rule Func`, str], optional
        Rule string or function to be used to run the simulation. Check the
        `game.rules` module to see available rules and rule strings. If not
        specified the rule defaults to the standard ``Conway's Game of Life``
        rule.

    alive, dead: str, optional
        Strings used to represent dead and alive cells. If not specified, alive
        cells are represented using ``•`` and dead cells using `` ``.


    Attributes
    ----------
    matrix: Matrix
        Current state of the life grid
    wrap: bool
        Whether to wrap the life grid around the edges
    rule: `callable` [[int, int, Neighbors], int]
        Rule to use when running the simulation
    out: `callable` [`Pipe`, None]
        Display function receiving a pipe end to read the current state of the
        game and display it.
    charmap: `dict` [`str`, `str`]
        Dict containing strings to display dead and alive cells

    Examples
    --------
    Running from an RLE file

    >>> from pygol.utils import parse_rle
    >>> from pygol.gui import pygame
    >>> conw = Game(**parse_rle(/path/to/seed.rle)).pad(20).pipe(pygame)
    >>> conw.run(100)

    Running a simulation in the terminal

    >>> import os
    >>> import time
    >>> conw = Game(width=170, height=50)
    >>> for i in range(100):
    ...     os.system("clear")
    ...     print(conw)
    ...     conw.tick()
    ...     time.sleep(0.5)

    """

    # pylint: disable=too-many-arguments
    def __init__(self, width: int, height: int, seed: List[List[Any]] = None,
                 wrap: bool = True, rule: Union[Rule, str] = conways_life,
                 alive: str = "•", dead: str = " ") -> Game:
        if not seed:
            seed = Matrix(width, height).fill_random()

        if isinstance(rule, str):
            try:
                rule = RULES[rule]
            except KeyError:
                rule = RULES[rule.upper()]

        super().__init__(width, height, seed)
        self.wrap = wrap
        self.rule = rule
        self.out = lambda x: None
        self.charmap = {
            "alive": alive,
            "dead": dead
        }

    def __str__(self) -> str:
        res = ""

        for row in self:
            for col in row:
                res += self.charmap["alive"] if col == 1 else self.charmap["dead"]
            res += "\n"

        return res

    def tick(self) -> Game:
        """Advance the simulation by one tick.

        Construct a new game state by applying the rule function to all cells.

        Returns
        -------
        self: Game
            Returns the game object to allow chaining.
        """
        grid = Matrix(self.width, self.height)
        nb = self.neighbors
        rule = self.rule

        for y in range(self.height):
            for x in range(self.width):
                cell = self[y][x]

                neighbors = nb(x, y, wrap=self.wrap)
                alive_count = sum([x for x, *_ in neighbors])

                grid[y][x] = rule(cell, alive_count, neighbors)

        self.matrix = grid
        return self

    def pipe(self, func: Callable[[mp.Pipe], None]) -> Game:
        """Save a display function.

        Parameters
        ----------
        func: `callable` [`Pipe`, None]
            Display function receiving a pipe end to read and display to current
            game state. See the ``gui`` module for example display functions.

        Returns
        -------
        self: Game
            Returns the game object to allow chaining.

        Notes
        -----
        The display function is spawned in a different process using the
        ``multiprocess`` module. It receives a pipe that it can read and write
        to. The pipe can be read using ``pipe.recv()`` and written to using
        ``pipe.send(payload)``. The display function should only write a
        ``SIGTERM`` signal into the pip when it is terminated. This signals the
        simulation process that it has been terminated, presumably by the user
        (e.g. by closing a pygame window).
        """
        self.out = func
        return self

    def run(self, times: int, delay: float = 0.1) -> Game:
        """Run the life simulation and call the display function

        Parameters
        ----------
        time: int
            Amount of ticks to run the simulation.
        delay: float, optional
            Delay between every frame of the simulation. Defaults to ``0.1``
            seconds.

        Returns
        -------
        self: Game
            Returns the game object to allow chaining.

        Notes
        -----
        The run function first writes the delay into the pipe before running the
        simulation and writing the game states to the pipe. The run function
        may terminate before having completed the specified number of ticks
        if it receives a ``SIGTERM`` signal from the display function.
        """
        read, write = mp.Pipe(duplex=True)

        display = mp.Process(target=self.out, args=(read,))
        display.start()

        write.send(delay)

        for _ in range(times):
            self.tick()
            write.send(self)

            # Check if display process ended (e.g. user closed window)
            if write.poll():
                display_ended = write.recv()
                if display_ended == SIGTERM:
                    break

        write.send(SIGTERM)
        read.close()
        display.join()
        return self
