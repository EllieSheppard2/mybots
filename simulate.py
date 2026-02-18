import pybullet as p
import pybullet_data
from sympy.physics.units import frequency

import pyrosim.pyrosim as pyrosim
import time
import numpy
import math
import random

amplitudeBackLeg = math.pi / 4.0
phaseOffsetBackLeg = 0.0

amplitudeFrontLeg = math.pi / 4.0
phaseOffsetFrontLeg = math.pi / 2.0

steps_in_sim=1000

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-19.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(steps_in_sim)
frontLegSensorValues = numpy.zeros(steps_in_sim)
print(backLegSensorValues)

phaseBackLeg = numpy.linspace(0, 10 * 2*math.pi, steps_in_sim)
targetAnglesBackLeg = amplitudeBackLeg * numpy.sin(phaseBackLeg + phaseOffsetBackLeg)

phaseFrontLeg = numpy.linspace(0, 10 * 2*math.pi, steps_in_sim)
targetAnglesFrontLeg = amplitudeFrontLeg * numpy.sin(phaseFrontLeg + phaseOffsetFrontLeg)
#numpy.save('data/targetAngles.npy', targetAngles)
#exit()

for i in range(steps_in_sim):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegSensorValues[i]=backLegTouch
    frontLegSensorValues[i]=frontLegTouch
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b'Torso_BackLeg',

        controlMode = p.POSITION_CONTROL,

        targetPosition = targetAnglesBackLeg[i],

    maxForce = 200)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b'Torso_FrontLeg',

        controlMode = p.POSITION_CONTROL,

        targetPosition = targetAnglesFrontLeg[i],

        maxForce = 200)
    time.sleep(1/240)

p.disconnect()

numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)