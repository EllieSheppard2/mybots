import numpy as np
import sys

class SOLUTION():
    def __init__(self):
        self.weights = np.random.rand(3, 2)

        self.weights = self.weights * 2 - 1