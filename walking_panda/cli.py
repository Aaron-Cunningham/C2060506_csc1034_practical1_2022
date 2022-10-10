import argparse
from . import panda


def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--scale", type=float, default=1, help="Enlarge panda * original size > scale = 1")

    parser.add_argument("--colour-blue", help="Makes the panda blue",
                        action="store_true")
    parser.add_argument("--pandas", type=int, default=1, help="Duplicate pandas")

    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
