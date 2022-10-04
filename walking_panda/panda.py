from math import pi, sin, cos
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

# Keymap functions default set to false
keyMap = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}


# function to update key map
def keyMapUpdate(key, state):
    keyMap[key] = state


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False, scale=1, colour_blue=False, pandas=1):

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

        # Sets the keymap functions to true when pressed and false when unpressed
        # Which updates keyMapUpdate
        self.accept("arrow_left", keyMapUpdate, ["left", True])
        self.accept("arrow_left-up", keyMapUpdate, ["left", False])

        self.accept("arrow_right", keyMapUpdate, ["right", True])
        self.accept("arrow_right-up", keyMapUpdate, ["right", False])

        self.accept("arrow_down", keyMapUpdate, ["up", True])
        self.accept("arrow_down-up", keyMapUpdate, ["up", False])

        self.accept("arrow_up", keyMapUpdate, ["down", True])
        self.accept("arrow_up-up", keyMapUpdate, ["down", False])

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

        # If statement to which runs if --pandas argument is run
        if pandas == 1:
            pass
        else:
            # List that stores the panda actors
            self.actors = []
            # loads in panda actor models in a for loop
            for x in range(0, pandas):
                self.actors.append(Actor("models/panda-model", {"walk": "models/panda-walk4"}))
            counter = 3
            # renders and sets the scale, position, and animation of the panda which is added to the actors list in a
            # for loop
            for x in self.actors:
                x.setScale(0.005, 0.005, 0.005)
                x.reparentTo(self.render)
                x.setPos(counter, 0, 0)
                counter += 3
                x.loop("walk")

        # Plays copyright free background music in a loop.
        pandaMusic = self.loader.loadSfx(
            '/Users/aaroncunningham/PycharmProjects/C2060506_csc1034_practical1_2022/sounds/Sneaky-Snitch.mp3')
        pandaMusic.setLoop(True)
        pandaMusic.play()

        # Sets pandas movement speed
        self.speed = 0.05
        # Runs update function
        self.taskMgr.add(self.updatePandaPos, "updatePandaPos")

    # function to update panda position on keypress
    def updatePandaPos(self, task):
        pos = self.pandaActor.getPos()
        # if statements to move panda on keypress
        if keyMap["left"]:
            pos.x -= self.speed
        if keyMap['right']:
            pos.x += self.speed
        if keyMap['up']:
            pos.y += self.speed
        if keyMap['down']:
            pos.y -= self.speed

        self.pandaActor.setPos(pos)
        return task.cont

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)

        return Task.cont
