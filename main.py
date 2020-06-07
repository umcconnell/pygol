"""PyGoL - Python Game of Life"""
from pygol.game import Game
from pygol.utils import parse_rle
from pygol.gui import pygame, terminal

from pygol.cli import ARGS

if ARGS.file:
    CONW = Game(**parse_rle(ARGS.file), wrap=ARGS.wrap).pad(ARGS.pad)
else:
    CONW = Game(width=ARGS.pad * 2, height=ARGS.pad * 2, wrap=ARGS.wrap,
                rule=ARGS.rule)

DISPLAY = pygame if ARGS.display == "pygame" else terminal

CONW.pipe(DISPLAY).run(ARGS.iter, delay=ARGS.delay)
