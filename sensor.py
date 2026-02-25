import numpy as np
import constants as c
import pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.steps_in_sim)
    def Get_Value(self, step):
        touchValue = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        self.values[step] = touchValue
        if step == c.steps_in_sim - 1:
            print(self.values)