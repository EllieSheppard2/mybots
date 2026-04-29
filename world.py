import pybullet as p
import random

class WORLD:
    def __init__(self):
        random.seed(42)
        for i in range(10):
            x = random.uniform(2, 10)
            y = random.uniform(-3, 3)
            colShape = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.5, 0.5, 0.5])
            visShape = p.createVisualShape(p.GEOM_BOX, halfExtents=[0.5, 0.5, 0.5],
                                           rgbaColor=[1, 0.5, 0, 1])
            p.createMultiBody(baseMass=0,
                              baseCollisionShapeIndex=colShape,
                              baseVisualShapeIndex=visShape,
                              basePosition=[x, y, 0.5])