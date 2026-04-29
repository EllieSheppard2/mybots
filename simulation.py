import pybullet as p
import pybullet_data
import constants as c
import time
from robot import ROBOT
from world import WORLD

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)
        p.loadURDF("plane.urdf")
        p.changeDynamics(0, -1, lateralFriction=10.0)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        for i in range(c.steps_in_sim):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/60)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
        p.disconnect()