from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from move_robot import go_line, robot_stop

ev3 = EV3Brick()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor= Motor(Port.B,  Direction.COUNTERCLOCKWISE)
# left_arm = Motor(Port.D)
# right_arm = Motor(Port.A)

color_1 = ColorSensor(Port.S1)
color_2 = ColorSensor(Port.S2)
color_3 = ColorSensor(Port.S3)
distance = UltrasonicSensor(Port.S4)



def step_1():
    robot = DriveBase(left_motor, right_motor, 56 , 158)
    robot.settings(1024, 1024, 1024)
    robot.turn(45)
    robot.straight(180)
    robot.turn(-25)