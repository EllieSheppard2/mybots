import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c


class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.motors = {}

        # Load robot body
        self.robotId = p.loadURDF("body.urdf")

        # Prepare simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        # Load unique brain file
        brainFile = "brain" + solutionID + ".nndf"
        self.nn = NEURAL_NETWORK(brainFile)

        # Delete brain file after loading
        os.system("rm " + brainFile)

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in ["BackLeg", "FrontLeg", "Torso"]:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in [b'Torso_BackLeg',
        b'Torso_FrontLeg',
        b'Torso_LeftLeg',
        b'Torso_RightLeg',
        b'FrontLeg_FrontLowerLeg',
        b'BackLeg_BackLowerLeg',
        b'LeftLeg_LeftLowerLeg',
        b'RightLeg_RightLowerLeg',]:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self, desiredAngle)

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        tmpFile = "tmp" + self.solutionID + ".txt"
        finalFile = "fitness" + self.solutionID + ".txt"

        # Write to temp file first
        with open(tmpFile, "w") as f:
            f.write(str(xCoordinateOfLinkZero))

        # Rename to final fitness file (avoids race conditions)
        os.rename(tmpFile, finalFile)