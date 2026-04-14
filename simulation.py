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
        p.loadURDF("plane.urdf")        # ← floor
        self.world = WORLD()            # ← blocks (before robot)
        self.robot = ROBOT(solutionID)  # ← robot on top

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