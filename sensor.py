import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.steps_in_sim)
    def Get_Value(self, step):
        try:
            touchValue = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        except TypeError:
            touchValue = -1.0
        self.values[step] = touchValue
        if step == c.steps_in_sim - 1:
            print(self.values)
    def Save_Values(self):
        np.save("data/" + self.linkName + "SensorValues.npy", self.values)