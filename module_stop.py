from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import*

from module_line import *
ev3 = EV3Brick()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor= Motor(Port.B,  Direction.COUNTERCLOCKWISE)
left_arm = Motor(Port.D)
right_arm = Motor(Port.A)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S2)
color_3 = ColorSensor(Port.S3)
#distance = UltrasonicSensor(Port.S4)
# "robot_stop" 함수
#  로봇을 정지하도록 하는 함수이다.
#   파라미터는 부드러운 정지를 원하면 stop, 모터 위치를 정지한 곳을 유지하고 싶을때는 hold,
#   흔히 말하는 일반 정지는 아무런 값도 입력하지 않으면 된다.
def robot_stop(text):
    if text == "stop" :
        left_motor.stop()
        right_motor.stop()

    elif text == "hold" :
        left_motor.hold()
        right_motor.hold()
        wait(200)
    else:
    # elif text == "brake":
        left_motor.brake()
        right_motor.brake()
