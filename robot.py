
""" 
Author: Kalei Foley-Rutherfurd
Description: ROBOT contains all properties of a ROBOT object

"""

import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

	def __init__(self):
		self.sensors = {}
		self.motors = {}

		self.robot_id = p.loadURDF("body.urdf")
		self.nn = NEURAL_NETWORK("brain.nndf") #create neural network

		pyrosim.Prepare_To_Simulate(self.robot_id)
		self.prepare_to_sense()
		self.prepare_to_act()


	def prepare_to_sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def prepare_to_act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def sense(self, i):
		for s in self.sensors.values():
			s.get_value(i)

	def act(self, i):
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[jointName].set_value(desiredAngle, self.robot_id)
				jointName = jointName.decode("utf-8")

	def think(self):
		self.nn.Update()
