import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

	def __init__(self, n):
		self.linkName = n
		self.values = numpy.zeros(c.STEPS)

	def get_value(self, t):
		self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName) 
		if t == c.STEPS-1:
			print(self.values)

	def save_values(self):
		numpy.save("data/" + self.linkName + "SensorValues.npy", self.values)