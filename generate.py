import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

rows = 5
cols = 5
height = 5
space = 1.0

for i in range(rows):
    for j in range(cols):

        size = 1.0
        z = size / 2.0

        x = i * space.
        y = j * space

        for k in range(height):
            pyrosim.Send_Cube(name=f"Box_{i}_{j}_{k}", pos=[x, y, z], size=[size, size, size])

            next_size = size * 0.9
            z += (size / 2.0) + (next_size / 2.0)
            size = next_size

pyrosim.End()