from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorSensor


# Initilize the color sensor
color_sensor = ColorSensor(Port.A)
color = color_sensor.color()
print (color)