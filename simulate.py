import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import math
import random

steps_in_sim=300

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

        targetPosition = random.uniform(-math.pi/2.0, math.pi/2.0),

        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex = robotId,

        jointName = b'Torso_FrontLeg',

        controlMode = p.POSITION_CONTROL,

        targetPosition = random.uniform(-math.pi/2.0, math.pi/2.0),

        maxForce = 500)
    time.sleep(1/500)

p.disconnect()

numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)