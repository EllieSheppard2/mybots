import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import os

from sensor import SENSOR
from motor import MOTOR
import constants as c

from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body.urdf", basePosition=[0, 0, 1.5], baseOrientation=p.getQuaternionFromEuler([0, 0, 0]))
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")

        os.system('rm brain' + str(self.solutionID) + '.nndf')

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName.encode("utf-8")].Set_Value(self, desiredAngle)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        basePosition = p.getBasePositionAndOrientation(self.robotId)[0]
        xPosition = basePosition[0]
        fitness = -xPosition

        tmpFile = "tmp" + self.solutionID + ".txt"
        finalFile = "fitness" + self.solutionID + ".txt"
        with open(tmpFile, "w") as f:
            f.write(str(fitness))
        os.rename(tmpFile, finalFile)

