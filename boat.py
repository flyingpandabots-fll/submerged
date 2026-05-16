from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()
# Set up 
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
arm = Motor(Port.B,Direction.COUNTERCLOCKWISE)

drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)

# speed (max speed : 900)
drive_base.settings(950, 950, 950, 950)
# Tell the drive base to use the gyro sensor for better accuracy.


#drive_base.straight(-150)
# drive forward the boat mission

drive_base.straight(-350)

drive_base.arc(radius=-60, angle=-45)

drive_base.straight(-45)

# solve boat mission
arm.run_angle(70,180,wait=True)

# go back to home
drive_base.straight(150)

drive_base.arc(radius=-50, angle=45)

drive_base.straight(250)