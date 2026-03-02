import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
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
        for motor in self.motors.values():
            motor.Set_Value(self, i)
    def Think(self):
        pass