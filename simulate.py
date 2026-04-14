from simulation import SIMULATION
from solution import SOLUTION
import sys
import time
import pybullet as p
import constants as c

directOrGUI = "GUI"

# Generate fresh body and brain
s = SOLUTION(0)
s.Create_World()
s.Create_Body()
s.Create_Brain()

solutionID = "0"

simulation = SIMULATION(directOrGUI, solutionID)

for i in range(c.steps_in_sim):
    simulation.robot.Sense(i)
    simulation.robot.Think()
    simulation.robot.Act(i)
    p.stepSimulation()

    if directOrGUI == "GUI":
        time.sleep(0.01)

simulation.Get_Fitness()