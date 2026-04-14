from simulation import SIMULATION
from solution import SOLUTION
import sys
import time
import pybullet as p
import constants as c
import numpy as np

directOrGUI = "GUI"

s = SOLUTION(0)
s.Create_World()
s.Create_Body()
s.Create_Brain()

solutionID = "0"
simulation = SIMULATION(directOrGUI, solutionID)

for i in range(c.steps_in_sim):
    t = i * 0.05
    amplitude = .5  # much larger movement

    joint_angles = {
        "Torso_BackLeg":           np.sin(t) * amplitude,
        "Torso_FrontLeg":          np.sin(t + np.pi) * amplitude,
        "Torso_LeftLeg":           np.sin(t) * amplitude,
        "Torso_RightLeg":          np.sin(t + np.pi) * amplitude,
        "FrontLeg_FrontLowerLeg":  np.sin(t + np.pi) * amplitude,
        "BackLeg_BackLowerLeg":    np.sin(t) * amplitude,
        "LeftLeg_LeftLowerLeg":    np.sin(t + np.pi) * amplitude,
        "RightLeg_RightLowerLeg":  np.sin(t) * amplitude,
    }

    for jointName, angle in joint_angles.items():
        simulation.robot.motors[jointName.encode("utf-8")].Set_Value(simulation.robot, angle)

    p.stepSimulation()
    if directOrGUI == "GUI":
        time.sleep(0.01)

simulation.Get_Fitness()