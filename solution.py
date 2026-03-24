import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import sys
import random


class SOLUTION:
    def __init__(self):
        # 3x2 matrix of random weights scaled to [-1, +1]
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
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # Sensor neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # Motor neurons
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # Send the synapses using self.weights
        for currentRow in [0, 1, 2]:  # sensor neurons
            for currentColumn in [0, 1]:  # motor neurons
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow,
                    targetNeuronName=currentColumn + 3,  # motor neuron offset
                    weight=weight
                )

        pyrosim.End()

    def Evaluate(self, mode = "DIRECT"):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system(f'"{sys.executable}" simulate.py {mode}')

        with open("fitness.txt", "r") as fitnessFile:
            self.fitness = float(fitnessFile.read())

    def Mutate(self):
        randomRow = random.randint(0, 2)

        randomColumn = random.randint(0, 1)

        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
