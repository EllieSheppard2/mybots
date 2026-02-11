import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy

steps_in_sim=100

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
    time.sleep(1/120)

p.disconnect()

numpy.save("data/backLegSensorValues.npy",backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy",frontLegSensorValues)