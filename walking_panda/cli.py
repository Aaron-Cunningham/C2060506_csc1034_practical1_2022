
def cli():
    walking = WalkingPanda()
    walking.run()
from . import panda

def cli():
    walking = panda.WalkingPanda()
    walking.run()