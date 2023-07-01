#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import*
# from step_1 import step_1


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left = Motor(Port.C)
right= Motor(Port.B)
#left_arm = Motor(Port.D)
#right_arm = Motor(Port.A)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S2)

#color_3 = ColorSensor(Port.S3)
#distance = UltrasonicSensor(Port.S4)

# 각자 구역을 정해 프로젝트를 완성합니다.
right.run_angle(500,700,Stop.BRAKE,False)
left.run_angle(500,700)
right_motor.run_angle(1000, 100)
left_motor.run_angle(1000, 100)

# while True:
#     print(color_1.reflection(),color_2.reflection())
