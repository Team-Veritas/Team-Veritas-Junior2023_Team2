from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import*

from module_device import *
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
left_arm = Motor(Port.D)
right_arm = Motor(Port.A)

color_1 = LightSensor(Port.S1)
color_2 = LightSensor(Port.S2)

color_3 = ColorSensor(Port.S3)
#distance = UltrasonicSensor(Port.S4)

#color_3 = ColorSensor(Port.S3)
#5distance = UltrasonicSensor(Port.S4)

# robot = DriveBase(left_motor, right_motor, 56 , 158)

# "go_line" 함수
#  컬러센서 2개를 이용하여 검정색 라인을 따라 이동한다.
#   파라미터는 이동시 속도, 모터의 각도 값이다.
def go_line(speed, degrees  ,a,b,c):

    # PID 상수 정의
    Kp = a
    Ki = b
    Kd = c

    # 오차 변수 초기화
    error = 0
    last_error = 0
    integral = 0

    # 메인 루프 정의
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    while (abs(right_motor.angle()) + abs(left_motor.angle())) / 2 < degrees:
        # 센서 값을 읽기
        left_value = color_1.reflection()
        right_value = color_2.reflection()
        
        # 오차 계산
        error = left_value - right_value
        
        # 비례 항 계산
        proportional = Kp * error
        
        # 적분 항 계산
        integral += Ki * error
        
        # 미분 항 계산
        derivative = Kd * (error - last_error)
        last_error = error
        
        # PID 출력 값 계산
        pid_output = int(proportional + integral + derivative)
        
        # PID 출력 값을 이용하여 모터 속도 설정
        left_speed = speed + pid_output
        right_speed = speed - pid_output
        left_motor.dc(left_speed)
        right_motor.dc(right_speed)


