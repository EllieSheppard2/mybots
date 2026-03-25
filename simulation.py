import pybullet as p
import pybullet_data
import constants as c
import numpy as np
import time
from robot import ROBOT
from world import WORLD

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)
        self.robot = ROBOT(solutionID)
        self.world = WORLD()

    def Run(self):
        phaseBackLeg = np.linspace(0, c.oscillation_range, c.steps_in_sim)
        self.targetAnglesBackLeg = c.amplitude_back_leg * np.sin(phaseBackLeg + c.phase_offset_back_leg)

        phaseFrontLeg = np.linspace(0, c.oscillation_range, c.steps_in_sim)
        self.targetAnglesFrontLeg = c.amplitude_front_leg * np.sin(phaseFrontLeg * 0.5 + c.phase_offset_front_leg)

        self.robot.motors[b'Torso_BackLeg'].motorValues = self.targetAnglesBackLeg
        self.robot.motors[b'Torso_FrontLeg'].motorValues = self.targetAnglesFrontLeg

        for i in range(c.steps_in_sim):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            time.sleep(1/160)
    def Get_Fitness(self):
        self.robot.Get_Fitness()
