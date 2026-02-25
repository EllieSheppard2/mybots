import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import time
import robot as robot

class SIMULATION:
    def __init__(self):
        self.robot = robot
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.gravity)

    def Run(self):
        self.backLegSensorValues = np.zeros(c.steps_in_sim)
        self.frontLegSensorValues = np.zeros(c.steps_in_sim)

        phaseBackLeg = np.linspace(0, c.oscillation_range, c.steps_in_sim)
        self.targetAnglesBackLeg = c.amplitude_back_leg * np.sin(phaseBackLeg + c.phase_offset_back_leg)

        phaseFrontLeg = np.linspace(0, c.oscillation_range, c.steps_in_sim)
        self.targetAnglesFrontLeg = c.amplitude_front_leg * np.sin(phaseFrontLeg + c.phase_offset_front_leg)

        for i in range(c.steps_in_sim):
            p.stepSimulation()
            self.robot.Sense(i)

            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robotId,
                jointName=b'Torso_BackLeg',
                controlMode=p.POSITION_CONTROL,
                targetPosition=self.targetAnglesBackLeg[i],
                maxForce=c.motor_max_force
            )

            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robotId,
                jointName=b'Torso_FrontLeg',
                controlMode=p.POSITION_CONTROL,
                targetPosition=self.targetAnglesFrontLeg[i],
                maxForce=200
            )
            time.sleep(100)

        np.save("data/backLegSensorValues.npy", self.backLegSensorValues)
        np.save("data/frontLegSensorValues.npy", self.frontLegSensorValues)