"""PyGoL CLI parser"""
import argparse

#: Argparse parser.
PARSER = argparse.ArgumentParser(description="Conway's Game of Life in Python")

PARSER.add_argument('display', choices=['terminal', 'pygame'],
                    help='Display to use for simulation')
PARSER.add_argument('-f', '--file', help='Path to RLE life pattern')
PARSER.add_argument('-i', '--iter', type=int, default=1000,
                    help='Number of iterations to run simulation; default is 1000')
PARSER.add_argument('-d', '--delay', type=float, default=0.07,
                    help='Delay in seconds between individual frames; default is 0.07s')
PARSER.add_argument('-p', '--pad', type=int, default=20,
                    help='Pixels of padding applied to life grids; default is 20')
PARSER.add_argument('-w', '--wrap', type=bool, default=True,
                    help='Whether or not to wrap simulation at edges; default is True')
PARSER.add_argument('-r', '--rule', default='B3/S23',
                    help="Rule string used for simulation; default is B3/S23")
