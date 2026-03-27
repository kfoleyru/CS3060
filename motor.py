import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

	def __init__(self, n):

		self.joint_name = n
		self.amp = c.AMPLITUDE
		self.freq = c.FREQUENCY
		self.offset = c.PHASE_OFFSET

		self.motor_values = numpy.linspace(0, 2 * c.PI, c.STEPS)

		if self.joint_name == b'Torso_BackLeg':
			self.motor_values == self.amp * numpy.sin((self.freq / 2) * self.motor_values + self.offset)
		else:
			self.motor_values = self.amp * numpy.sin(self.freq * self.motor_values + self.offset)
	
	def set_value(self, desired_angle, robot_id):
		pyrosim.Set_Motor_For_Joint(
			bodyIndex = robot_id, 
			jointName = self.joint_name,
			controlMode = p.POSITION_CONTROL,
			targetPosition = desired_angle,
			maxForce = c.MAX_FORCE
		)

	def save_values(self):
		numpy.save("data/" + self.joint_name + "MotorTargetValues.npy", self.motor_values)