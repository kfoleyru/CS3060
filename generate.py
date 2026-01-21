import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# size variables
l = 1
w = 1
h = 1

# position variables
x = 0
y = 0
z = h/2

pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[l,w,h])
pyrosim.Send_Cube(name="Box2", pos=[x,y,z+h] , size=[l,w,h])

pyrosim.End()

