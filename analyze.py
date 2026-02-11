import matplotlib.pyplot as pyplot
import numpy

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

pyplot.plot(backLegSensorValues, label="Back Leg Sensor Values")
pyplot.plot(frontLegSensorValues, label="Front Leg Sensor Values")

pyplot.legend(loc="upper right")

pyplot.show()