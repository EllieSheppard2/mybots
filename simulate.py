from simulation import SIMULATION
import sys
import time
import pybullet as p
import constants as c

directOrGUI = sys.argv[1] if len(sys.argv) > 1 else "DIRECT"
simulation = SIMULATION(directOrGUI)

for i in range(c.steps_in_sim):
    simulation.robot.Sense(i)
    simulation.robot.Think()
    simulation.robot.Act(i)
    p.stepSimulation()

    if directOrGUI == "GUI":
        time.sleep(0.01)

simulation.Get_Fitness()