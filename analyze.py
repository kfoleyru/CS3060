import matplotlib.pyplot as pyplot
import numpy

# backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
# frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

# pyplot.plot(backLegSensorValues, label="Back Leg Sensor Values", linewidth=0.5)
# pyplot.plot(frontLegSensorValues, label="Front Leg Sensor Values", linewidth=0.5)

targetAngleValuesB = numpy.load('data/targetAngleValuesBack.npy')
targetAngleValuesF = numpy.load('data/targetAngleValuesFront.npy')


pyplot.plot(targetAngleValuesB, label="Back Leg Target Angle Values", linewidth=1)
pyplot.plot(targetAngleValuesF, label="Front Leg Target Angle Values", linewidth=1)

pyplot.legend(loc="upper right")

pyplot.show()