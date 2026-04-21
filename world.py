import pybullet as p

class WORLD:
    def __init__(self):
        for x in range(1, 4):
            colShape = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.5, 0.5, 0.5])
            visShape = p.createVisualShape(p.GEOM_BOX, halfExtents=[0.5, 0.5, 0.5],
                                           rgbaColor=[1, 0.5, 0, 1])
            p.createMultiBody(baseMass=0,
                              baseCollisionShapeIndex=colShape,
                              baseVisualShapeIndex=visShape,
                              basePosition=[-(x * 2), 0, 0.5])