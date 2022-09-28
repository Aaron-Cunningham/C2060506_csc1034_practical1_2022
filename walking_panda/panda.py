import argparse
from math import pi, sin, cos
from playsound import playsound
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False):
        ShowBase.__init__(self, )
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Changes the camera position to see panda
        self.cam.set_pos(0, -10., 1.5)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.

        if no_rotate == False:
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        #Plays background music in a loop
        pandaMusic = self.loader.loadSfx('/Users/aaroncunningham/PycharmProjects/C2060506_csc1034_practical1_2022/sounds/Sneaky-Snitch.mp3')
        pandaMusic.setLoop(True)
        pandaMusic.play()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)

        return Task.cont
