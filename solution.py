import sys
import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import time
import random
import constants as c


class SOLUTION:
    def __init__(self, ID):
        self.myID = ID
        self.weights = np.random.rand(3, 2) * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        x, y, z = -2, 0, 0.5
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
        # Back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[-0.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        # Front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[0.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):
        fileName = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(fileName)

        for i, linkName in enumerate(["Torso", "BackLeg", "FrontLeg"]):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=linkName)

        for j, jointName in enumerate(["Torso_BackLeg", "Torso_FrontLeg"]):
            pyrosim.Send_Motor_Neuron(
                name=j + c.numSensorNeurons,
                jointName=jointName
            )

        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                weight = self.weights[i][j]
                pyrosim.Send_Synapse(
                    sourceNeuronName=i,
                    targetNeuronName=j + c.numSensorNeurons,
                    weight=weight
                )

        pyrosim.End()
        exit()

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system(sys.executable + " simulate.py " + mode + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fileName = "fitness" + str(self.myID) + ".txt"

        while not os.path.exists(fileName):
            time.sleep(0.01)

        with open(fileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

        os.system("rm " + fileName)

    def Mutate(self):
        randomRow = random.randint(0, 2)

        randomColumn = random.randint(0, 1)

        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID