#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import*



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
from step_1 import*
from module_stop import*
from module_line import*
# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
left_arm = Motor(Port.D)
right_arm = Motor(Port.A)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S2)

color_3 = ColorSensor(Port.S3)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S2)

color_3 = ColorSensor(Port.S3)
#distance = UltrasonicSensor(Port.S4)

# 각자 구역을 정해 프로젝트를 완성합니다.
step_1()