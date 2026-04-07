import pyrosim.pyrosim as pyrosim

# size variables
LENGTH = 1
WIDTH = 1
HEIGHT = 1

def create_world():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.End()

def generate_body():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name = "Torso", pos=[0,0,1.5], size=[LENGTH,WIDTH,HEIGHT])
	pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , 
							type = "revolute", position = [0.5,0,1])
	pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , 
							type = "revolute", position = [-0.5,0,1])
	pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[LENGTH,WIDTH,HEIGHT])
	pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[LENGTH,WIDTH,HEIGHT])


	pyrosim.End()

def generate_brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	
	pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
	pyrosim.Send_Sensor_Neuron(name = 1, linkName = "FrontLeg")
	pyrosim.Send_Sensor_Neuron(name = 2, linkName = "BackLeg")
	
	pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
	pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
	
	# connect neuron 1 to neuron 3
	pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 3, weight = 1.0)
	pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 3, weight = 1.0)
	pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = 0.0)
	pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 4, weight = 0.0)


	pyrosim.End()


if __name__ == "__main__":
	create_world()
	generate_body()
	generate_brain()