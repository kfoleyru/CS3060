import numpy
import os

class SOLUTION:

	def __init__(self):
		
		# matrix of 3 rows, 2 columns
		self.weights = numpy.random.rand(3,2) * 2 - 1

	def evaluate(self):
		os.system("python simulate.py")

	def create_world(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.End()

	def generate_body(self):
		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])
		pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1])
		pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
		pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[-0.5, 0, 1])
		pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

		pyrosim.End()

	def generate_brain(self):
		pyrosim.Start_NeuralNetwork("brain.nndf")

		pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
		pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
		pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

		pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
		pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

		# fill i-rows x j-cols matrix for sensor and motor neuron pairs
		for current_row in range(3): #3 sensor neurons
			for current_col in range(3, 5): #2 motor neurons
				pyrosim.Send_Synapse(sourceNeuronName = current_row, targetNeuronName = current_col+3, weight = self.weights[current_row, current_col])

		pyrosim.End()