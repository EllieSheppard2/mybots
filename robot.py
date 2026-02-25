import pybullet as p
import pyrosim
from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.Prepare_To_Sense()
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in ["BackLeg", "FrontLeg", "Torso"]:
            self.sensors[linkName] = SENSOR(linkName)
    def Sense(self, step):
        for sensor in self.sensors.values():
            sensor.Get_Value(step)