

from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()
Hub
# Set up 
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)

drive_base.settings(900, 800, 900,800) 

# Move forward 40 cm (400 mm)
drive_base.straight(-150)
drive_base.arc(-300, -91)

# Move backward 40 cm (400 mm)
drive_base.straight(-260)
drive_base.straight(10)
drive_base.arc(750, 37)
drive_base.arc(-60, -120)
drive_base.straight(-450)

