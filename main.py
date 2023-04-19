#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from move_robot import *
from step_1 import step_1


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor= Motor(Port.B,  Direction.COUNTERCLOCKWISE)
left_arm = Motor(Port.D)
right_arm = Motor(Port.A)

color_1 = ColorSensor(Port.S1)
color_2 = ColorSensor(Port.S2)
color_3 = ColorSensor(Port.S3)
distance = UltrasonicSensor(Port.S4)

# 각자 구역을 정해 프로젝트를 완성합니다.
strart()
step_1()
step_2()
step_3()
step_4()