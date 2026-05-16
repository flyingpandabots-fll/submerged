from pybricks.pupdevices import Motor
from pybricks.parameters import Port,Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the drive motors and arm
arm = Motor(Port.C)
left_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E,Direction.CLOCKWISE)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)
# Make both motors run at 500 degrees per second.
drive_base.use_gyro(True)
print(arm.angle())
#arm.reset_angle(0)

print(arm.angle())
#arm move down
arm.run_target(100,5,wait=True)
#move back code
drive_base.straight(-140)

#arm reset
arm.run_target(100,70,wait=True)
#arm.run_target(50,10)
#drive_base.straight(-100)

drive_base.turn(-40)
drive_base.turn(15)
##arm.run_target(100,0,wait=True)
drive_base.straight(150)


