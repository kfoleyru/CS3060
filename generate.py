import pyrosim.pyrosim as pyrosim

# size variables
LENGTH = 1
WIDTH = 1
HEIGHT = 1

def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.End()

def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5], size=[LENGTH,WIDTH,HEIGHT])
	pyrosim.Send_Joint( name = "Torso_Front_Leg" , parent= "Torso" , child = "Front_Leg" , 
							type = "revolute", position = [0.5,0,1])
	pyrosim.Send_Joint( name = "Torso_Back_Leg" , parent= "Torso" , child = "Back_Leg" , 
							type = "revolute", position = [-0.5,0,1])
	pyrosim.Send_Cube(name="Front_Leg", pos=[0.5,0,-0.5], size=[LENGTH,WIDTH,HEIGHT])
	pyrosim.Send_Cube(name="Back_Leg", pos=[-0.5,0,-0.5], size=[LENGTH,WIDTH,HEIGHT])
	pyrosim.End()

if __name__ == "__main__":
	Create_World()
	Create_Robot()