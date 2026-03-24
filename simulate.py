from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]

simulation = SIMULATION()
simulation.Run()
simulation.Get_Fitness()