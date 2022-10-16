import argparse
from . import panda


def cli():
    "Arguments which can be used in the terminal"
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help="Suppress Rotation",
                        action="store_true")
    #Allows no rotate on the panda

    parser.add_argument("--scale", type=float, default=1, help="Enlarge panda * original size > scale = 1")
    #Argument to make the panda larger or smaller depending on input

    parser.add_argument("--colour-blue", help="Makes the panda blue",
                        action="store_true")
    #Argument to change the panda colour to blue

    parser.add_argument("--pandas", type=int, default=1, help="Duplicate pandas")
    #Argument to add more pandas

    parser.add_argument("--animation", help="see the panda walking back and forth",
                        action="store_true")
    #Argument which simulates the panda moving
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()
