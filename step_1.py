from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import*
from module_line import*
from module_stop import*

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor= Motor(Port.C)
left_arm = Motor(Port.D)
right_arm = Motor(Port.A)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S2)
color_3 = ColorSensor(Port.S3)
# color_3 = ColorSensor(Port.S3)
# distance = UltrasonicSensor(Port.S4)


def step_1():
    robot = DriveBase(left_motor, right_motor, 56 , 158)

    


    right_motor.run_angle(300,250)
    left_motor.run_angle(300,250)
    robot.stop()
    
    go_line(55,750,0.6, 0.0001, 10)
    robot_stop("hold")
    wait(500)
    robot.stop()
    
    robot.straight(40)
    right_arm.run_angle(-300,500)
    robot.straight(40)
    right_arm.run_angle(-300,300)
    robot.straight(-210)
    robot.stop()
    right_motor.run_angle(300,400)
    robot.stop()
    go_line(55,1300,0.6, 0.0001, 10)
    robot_stop("hold")
    robot.turn(-60)
    robot.straight(-300)
    robot.straight(90)
    robot.turn(-60)
    robot.straight(20)
    robot.stop
    right_arm.run_angle(300,350)
    robot.stop
    robot.straight(-70)
    robot.turn(60)
    robot.straight(-150)
    robot.straight(230)
    robot.turn(60)
    robot.stop()
    go_line(55,850,0.6, 0.0001, 10)
    robot_stop("hold")
    robot.straight(70)
    robot.turn(-60)
    robot.stop()
    go_line(55,250,0.6, 0.0001, 10)
    robot_stop("hold")
    robot.straight(50)
    robot.turn(-60)
    
    

