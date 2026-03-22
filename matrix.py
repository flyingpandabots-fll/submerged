from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Icon,Port, Direction
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
# Initialize the hub.
hub = PrimeHub()
drivebase = DriveBase(Motor(Port.A, Direction.COUNTERCLOCKWISE), Motor(Port.E,Direction.CLOCKWISE), wheel_diameter=56, axle_track=114)
drivebase.use_gyro(True)
# Order: straight_speed, straight_acceleration, turn_rate, turn_acceleration
drivebase.settings(977, 400, 977, 100)
drivebase.straight(400, wait=True)
drivebase.arc(-160,angle=90, wait=True)