import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

	def __init__(self, name):
		self.linkName = name
		self.values = numpy.zeros(c.steps)

	def Get_Value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName) 
		if t == c.steps-1:
			print(self.values)