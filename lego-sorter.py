from pybricks.parameters import Color
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port

# Initilize the ColorSensor

color_sensor = ColorSensor(Port.A)
color = color_sensor.color()
print (color)