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
drive_base.settings(900, 900, 900, 900)

# Move forward 40 cm (400 mm)
drive_base.straight(400,Stop.NONE,False)

# Move backward 40 cm (400 mm)
#drive_base.straight(-400)

#display smiley face
Hub.display.icon(Icon.HAPPY,)
wait(2000)
