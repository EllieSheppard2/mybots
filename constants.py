import math

#moving leg
amplitude_back_leg = math.pi / 7.0
phase_offset_back_leg = 0.0

amplitude_front_leg = math.pi / 5.0
phase_offset_front_leg = math.pi / 2
#settings for simulation

steps_in_sim = 1000
gravity = -19.8
motor_max_force = 200
sleep_time = 1/240
oscillation_range = 10 * 2 * math.pi