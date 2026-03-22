""" 
Author: Kalei Foley-Rutherfurd
Description: ROBOT contains all properties of a ROBOT object

"""

import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:

	def __init__(self):

		self.robotId = p.loadURDF("body.urdf")

		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()


	def Prepare_To_Sense(self):
		# Empty dict to fill with instances of SENSOR
		self.sensors = {}

		# Empty dict to fill with instances of MOTOR
		self.motors = {}

		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)


	def Sense(self, t):
		for i in self.sensors:
			self.sensors[i].Get_Value(t)

