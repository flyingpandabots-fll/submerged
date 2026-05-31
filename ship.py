from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()
# Set up 
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)

# speed (max speed : 900)
drive_base.settings(700, 700, 700,700) 

# Move forward 40 cm (400 mm)
#drive_base.straight(100)
#drive_base.arc(-300, 91)
#drive_base.straight(200)

# Move backward 40 cm (400 mm)
drive_base.straight(-170)
drive_base.arc(-300, -91)
drive_base.straight(-140)

#back to coral
drive_base.straight(50)
drive_base.arc(600,37)

#drive_base.settings(100, 100, 100, 100)
#drive_base.straight(-260)
#drive_base.straight(320)
#rive_base.arc(-300,120)

