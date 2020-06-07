"""PyGoL GUI Module"""
# pylint: disable=wrong-import-position

# Import position is important! The `PYGAME_HIDE_SUPPORT_PROMT` environment
# variable must be set before we import pygame
# In VSCode save this file using Ctrl+K S to prevent formatting
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from .pygame import display as pygame
from .terminal import display as terminal
