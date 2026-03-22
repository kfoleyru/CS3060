"""
Author: Kalei Foley-Rutherfurd
Description: SIMULATION class contains all the properties of the
	simulation object

"""

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import constants as c

class SIMULATION:
	def __init__(self):

		self.physicsClient = p.connect(p.GUI)

		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) # hide GUI menus
		p.setGravity(0,0,-9.8, self.physicsClient) # set gravity

		self.world = WORLD()
		self.robot = ROBOT()

		pyrosim.Prepare_To_Simulate(self.robot.robotId)

	def Run(self):
		for step in range(c.steps):
			p.stepSimulation()
			self.robot.Sense(step)
			# print(i)
			# backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
			# frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
			# pyrosim.Set_Motor_For_Joint(
			# 	bodyIndex = robotId, 
			# 	jointName = b'Torso_BackLeg',
			# 	controlMode = p.POSITION_CONTROL,
			# 	targetPosition = targetAnglesB[i],
			# 	maxForce = 25)
			# pyrosim.Set_Motor_For_Joint(
			# 	bodyIndex = robotId, 
			# 	jointName = b'Torso_FrontLeg',
			# 	controlMode = p.POSITION_CONTROL,
			# 	targetPosition = targetAnglesF[i],
			# 	maxForce = 25)
			time.sleep(0.001)

		p.disconnect()

	def __del__(self):
		p.disconnect()