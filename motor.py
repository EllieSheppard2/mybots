import pyrosim.pyrosim
import pybullet as p
import numpy as np

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = []

    def Set_Value(self, robot, i):
        pyrosim.pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[i],
            maxForce=200
        )
    def Save_Values(self):
        np.save("data/" + str(self.jointName) + "MotorValues.npy", self.motorValues)