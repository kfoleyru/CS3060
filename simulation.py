from world import WORLD
from robot import ROBOT
import constants as c
import generate as g
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
	def __init__(self):
		self.physicsClient = p.connect(p.GUI)
		p.setAdditionalSearchPath(pybullet_data.getDataPath())
		p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) # hide GUI menus
		p.setGravity(0,0,-9.8, self.physicsClient) # set gravity

		self.world = WORLD()
		self.robot = ROBOT()

		pyrosim.Prepare_To_Simulate(self.robot.robot_id)

	def __del__(self):
		p.disconnect()

	def run(self):
		for step in range(c.STEPS):
			p.stepSimulation()
			self.robot.sense(step)
			self.robot.prepare_to_act()
			self.robot.act(step)
			
			time.sleep(0.001)