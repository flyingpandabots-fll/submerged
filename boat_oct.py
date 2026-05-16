from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()
# Set up 
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
arm = Motor(Port.C,Direction.COUNTERCLOCKWISE)

drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)

# speed (max speed : 900)
drive_base.settings(950, 950, 950, 950)
# Tell the drive base to use the gyro sensor for better accuracy.
# solve boat mission
arm.run_angle(70,180,wait=True)