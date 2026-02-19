# import constants as c
# import numpy
# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import random
# import time

# steps = 5000
# pi = numpy.pi


# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# p.setGravity(0,0,-9.8,physicsClient)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# amplitudeB = c.amplitudeB
# frequencyB = c.frequencyB
# phaseOffsetB = c.phaseOffsetB

# amplitudeF = c.amplitudeF
# frequencyF = c.frequencyF
# phaseOffsetF = c.phaseOffsetF

# backLegSensorValues = numpy.zeros(steps)
# frontLegSensorValues = numpy.zeros(steps)
# targetAnglesB = amplitudeB * numpy.sin(frequencyB * numpy.linspace(0, 2*pi, steps) + phaseOffsetB)
# targetAnglesF = amplitudeF * numpy.sin(frequencyF * numpy.linspace(0, 2*pi, steps) + phaseOffsetF)

# # numpy.save('data/targetAngleValuesBack.npy', targetAnglesB)
# # numpy.save('data/targetAngleValuesFront.npy', targetAnglesF)

# # # exit()

# for i in range(steps):
# 	p.stepSimulation()
# 	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	pyrosim.Set_Motor_For_Joint(
# 		bodyIndex = robotId, 
# 		jointName = b'Torso_BackLeg',
# 		controlMode = p.POSITION_CONTROL,
# 		targetPosition = targetAnglesB[i],
# 		maxForce = 25)
# 	pyrosim.Set_Motor_For_Joint(
# 		bodyIndex = robotId, 
# 		jointName = b'Torso_FrontLeg',
# 		controlMode = p.POSITION_CONTROL,
# 		targetPosition = targetAnglesF[i],
# 		maxForce = 25)
# 	time.sleep(0.001)

# numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
# numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)

# p.disconnect()

pass