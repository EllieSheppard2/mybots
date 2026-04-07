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
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        x, y, z = -2, 0, 0.5
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        # Back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                           type="revolute", position=[0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        # Front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                           type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(
            name="Torso_LeftLeg",
            parent="Torso",
            child="LeftLeg",
            type="revolute",
            position=[-0.5, 0, 1],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="LeftLeg",
            pos=[-0.5, 0, 0],
            size=[1, 0.2, 0.2]
        )

        pyrosim.Send_Joint(
            name="Torso_RightLeg",
            parent="Torso",
            child="RightLeg",
            type="revolute",
            position=[0.5, 0, 1],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="RightLeg",
            pos=[0.5, 0, 0],
            size=[1, 0.2, 0.2]
        )

        pyrosim.Send_Joint(
            name="RightLeg_RightLowerLeg",
            parent="RightLeg",
            child="RightLowerLeg",
            type="revolute",
            position=[0, 0, -1],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="RightLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 1, 0.2]
        )

        pyrosim.Send_Joint(
            name="FrontLeg_FrontLowerLeg",
            parent="FrontLeg",
            child="FrontLowerLeg",
            type="revolute",
            position=[0, 0, -1],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="FrontLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 1, 0.2]
        )

        pyrosim.Send_Joint(
            name="BackLeg_BackLowerLeg",
            parent="BackLeg",
            child="BackLowerLeg",
            type="revolute",
            position=[0, 0, -1],
            jointAxis="1 0 0"
        )

        pyrosim.Send_Cube(
            name="BackLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 1, 0.2]
        )

        pyrosim.Send_Joint(
            name="LeftLeg_LeftLowerLeg",
            parent="LeftLeg",
            child="LeftLowerLeg",
            type="revolute",
            position=[0, 0, -1],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="LeftLowerLeg",
            pos=[0, 0, -0.5],
            size=[1, 0.2, 0.2]
        )
        pyrosim.End()

    def Create_Brain(self):
        fileName = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(fileName)

        for i, linkName in enumerate(["Torso", "BackLeg", "FrontLeg", "RightLeg", "LeftLeg", "FrontLowerLeg", "BackLowerLeg", "FrontLowerLeg", "LeftLowerLeg", "RightLowerLeg" ]):
            pyrosim.Send_Sensor_Neuron(name=i, linkName=linkName)

        for j, jointName in enumerate(["Torso_BackLeg", "Torso_FrontLeg", "Torso_RightLeg", "Torso_LeftLeg", "FrontLeg_FrontLowerLeg", "BackLeg_BackLowerLeg", "LeftLeg_LeftLowerLeg", "RightLeg_RightLowerLeg"]):
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

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        time.sleep(0.1)

        os.system(sys.executable + " simulate.py " + mode + " " + str(self.myID) + " 2>&1 &")

    def Wait_For_Simulation_To_End(self):
        fileName = "fitness" + str(self.myID) + ".txt"

        while not os.path.exists(fileName):
            time.sleep(0.01)

        with open(fileName, "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

        os.system("rm " + fileName)

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)

        randomColumn = random.randint(0, c.numMotorNeurons - 1)

        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID