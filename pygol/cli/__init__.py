"""PyGoL Command Line Interface"""
from .cli import PARSER

#: Parsed arguments from argparse. Import this to access user settings
ARGS = PARSER.parse_args()
