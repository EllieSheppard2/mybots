import math

#moving leg
amplitude_back_leg = math.pi / 7.0
phase_offset_back_leg = 0.0

amplitude_front_leg = math.pi / 50
phase_offset_front_leg = math.pi / 20
#settings for simulation

steps_in_sim = 1000
gravity = -9.8
motor_max_force = 500
sleep_time = .01
oscillation_range = 10 * 2 * math.pi

numberOfGenerations = 50

populationSize = 15

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 2.0