import pybullet as p
import time


physicsClient = p.connect(p.GUI)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

while p.isConnected():
	p.stepSimulation()
	time.sleep(0.000001)

p.disconnect()