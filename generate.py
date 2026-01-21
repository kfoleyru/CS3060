import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

# size variables
LENGTH = 1
WIDTH = 1
HEIGHT = 1

# position variables
x = 0
y = 0
z = HEIGHT/2

#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[l,w,h])
# pyrosim.Send_Cube(name="Box2", pos=[x,y,z+h] , size=[l,w,h])

cubes = 0
for xax in range(5):
	x = xax
	# set value for first row
	for yax in range(5):
		y = yax
		#reset l,w,h
		l=LENGTH
		w=WIDTH
		h=HEIGHT
		for i in range(10):		
			pyrosim.Send_Cube(name="Box", pos=[x,y,z+i] , size=[l,w,h])
			#updated l,w,h
			l = .9*l
			w = .9*w
			h = .9*h

pyrosim.End()
