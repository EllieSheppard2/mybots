import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    x,y,z = -2,0,.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[1,1,1])
    #Adding boxes in a pattern
    for x in range(1, 6):
        for y in [-2, 0, 2]:
            pyrosim.Send_Cube(
                name=f"Box_{x}_{y}",
                pos=[x * 2, y, 0.5],
                size=[1, 1, 1]
            )
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",
                       type="revolute", position=[-0.5, 0, 1], jointAxis= "1 0 0")

    pyrosim.Send_Cube(name="BacpkLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",
                       type="revolute", position=[0.5, 0, 1], jointAxis= "1 0 0")

    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    sensor_neurons = [0, 1, 2]
    motor_neurons = [3, 4]
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    for i in sensor_neurons:
        for j in motor_neurons:
            random_weight = random.uniform(-1, 1)
            pyrosim.Send_Synapse(
                sourceNeuronName=i,
                targetNeuronName=j,
                weight= random_weight
            )

    pyrosim.End()



Create_World()
Generate_Body()
Generate_Brain()