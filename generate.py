import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1])
size = 1.0
a = size / 2
for i in range(10):
    pyrosim.Send_Cube(name=f"Box{i}", pos=[0,0,a] , size=[size, size, size])

    new_size = size * 0.9
    a = a + 1
    size = new_size

pyrosim.End()