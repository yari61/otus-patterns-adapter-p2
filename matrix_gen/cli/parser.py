from __future__ import annotations
from argparse import ArgumentParser

parser = ArgumentParser("matrix-gen")
parser.add_argument("-o", "--output", type=str, metavar='PATH', default="f0.json", help="path to output file")
