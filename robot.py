import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in ["BackLeg", "FrontLeg", "Torso"]:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in [b'Torso_BackLeg', b'Torso_FrontLeg']:
            self.motors[jointName] = MOTOR(jointName)
    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self, desiredAngle)
                print(neuronName, jointName, desiredAngle)
        #for motor in self.motors.values():
         #   motor.Set_Value(self, i)
    def Think(self):
        self.nn.Update()
        self.nn.Print()
