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

pass
#amplitudeBackLeg = c.amplitude_back_leg
#phaseOffsetBackLeg = c.phase_offset_back_leg

#amplitudeFrontLeg = c.amplitude_front_leg
#phaseOffsetFrontLeg = c.phase_offset_front_leg

#steps_in_sim= c.steps_in_sim

#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.setGravity(0, 0, c.gravity)
#planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")

#pyrosim.Prepare_To_Simulate(robotId)
#backLegSensorValues = numpy.zeros(c.steps_in_sim)
#frontLegSensorValues = numpy.zeros(c.steps_in_sim)
#print(backLegSensorValues)

#phaseBackLeg = numpy.linspace(0, c.oscillation_range, c.steps_in_sim)
#targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(phaseBackLeg + phaseOffsetBackLeg)

#phaseFrontLeg = numpy.linspace(0, c.oscillation_range, c.steps_in_sim)
#targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(phaseFrontLeg + phaseOffsetFrontLeg)
#numpy.save('data/targetAngles.npy', targetAngles)
#exit()

#for i in range(steps_in_sim):
 #   p.stepSimulation()
  #  backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
   # frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    #backLegSensorValues[i]=backLegTouch
    #frontLegSensorValues[i]=frontLegTouch
    #pyrosim.Set_Motor_For_Joint(

     #   bodyIndex = robotId,

      #  jointName = b'Torso_BackLeg',

       # controlMode = p.POSITION_CONTROL,

        #targetPosition = targetAnglesBackLeg[i],

   # maxForce = c.motor_max_force)
    #pyrosim.Set_Motor_For_Joint(

     #   bodyIndex = robotId,

      #  jointName = b'Torso_FrontLeg',

       # controlMode = p.POSITION_CONTROL,

        #targetPosition = targetAnglesFrontLeg[i],

       # maxForce = 200)
 #   time.sleep(c.sleep_time)

#p.disconnect()

#numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
#numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)