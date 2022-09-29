import argparse
from math import pi, sin, cos
from playsound import playsound
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False, scale=1, colour_blue=False):

        ShowBase.__init__(self)
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Changes the camera position to see panda
        self.cam.set_pos(0, -10., 1.5)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)



        # Uses scale argument to change size of panda
        if scale:
            # Load and transform the panda actor.
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005 * scale, 0.005 * scale, 0.005 * scale)

            self.pandaActor.reparentTo(self.render)
            # Loop its animation.
            self.pandaActor.loop("walk")

            # Makes the Panda blue if argument is run
        if colour_blue:
            pass
            self.pandaActor.setColor(0.12, 0.33, 0.9, 0.8)

        # If statement to run no_rotate argument
        if no_rotate:
            pass
        else:
            # Add the spinCameraTask procedure to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Plays copyright free background music in a loop.
        pandaMusic = self.loader.loadSfx(
            '/Users/aaroncunningham/PycharmProjects/C2060506_csc1034_practical1_2022/sounds/Sneaky-Snitch.mp3')
        pandaMusic.setLoop(True)
        pandaMusic.play()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)

        return Task.cont
