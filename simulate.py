from simulation import SIMULATION
import pybullet as p
import pybullet_data
import constants as c
from sympy.physics.units import frequency
import pyrosim.pyrosim as pyrosim
import time
import numpy
import math
import random

from simulation import SIMULATION
from world import WORLD
from robot import ROBOT


#amplitudeBackLeg = c.amplitude_back_leg
#phaseOffsetBackLeg = c.phase_offset_back_leg

#amplitudeFrontLeg = c.amplitude_front_leg
#phaseOffsetFrontLeg = c.phase_offset_front_leg

#steps_in_sim= c.steps_in_sim

simulation = SIMULATION()
world = WORLD()
robot = ROBOT()

#print(backLegSensorValues)

#phaseBackLeg = numpy.linspace(0, c.oscillation_range, c.steps_in_sim)
#targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(phaseBackLeg + phaseOffsetBackLeg)

#phaseFrontLeg = numpy.linspace(0, c.oscillation_range, c.steps_in_sim)
#targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(phaseFrontLeg + phaseOffsetFrontLeg)
#numpy.save('data/targetAngles.npy', targetAngles)
#exit()

