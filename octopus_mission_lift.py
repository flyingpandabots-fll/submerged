from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()
# Set up 
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
arm = Motor(Port.F,Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)

# speed (max speed : 900)
drive_base.settings(900, 900, 900, 900)

# Move forward 40 cm (400 mm)
drive_base.straight(480)

# Move backward 40 cm (400 mm)
drive_base.straight(-250)

drive_base.arc(radius=-50, angle=-20)

drive_base.straight(300)

drive_base.arc(radius=-50, angle=30)

arm.run_angle(43,-150)

drive_base.straight(475)



arm.run_angle(43,150)
