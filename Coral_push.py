

from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor
from pybricks.parameters import Icon, Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import PrimeHub
Hub = PrimeHub()

arm = Motor(Port.C, Direction.CLOCKWISE)

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
drive_base = DriveBase(left_motor, right_motor, 55,115)
drive_base.use_gyro(True)
drive_base.settings(900, 900, 900, 900)
drive_base.straight(200)
arm.run_angle(900, 250, wait=True)
arm.run_angle(900, -250, wait=True)
drive_base.straight(-200)