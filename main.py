from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

ev3 = EV3Brick()

# Motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor = Motor(Port.C)

# Sensors
ultraSS = UltrasonicSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)

def drive_forward(speed=200):
    left_motor.run(speed)
    right_motor.run(speed)

def stop():
    left_motor.stop()
    right_motor.stop()

def pick_ball():
    arm_motor.run_angle(200, 90)   # lower scoop
    wait(500)
    arm_motor.run_angle(200, -90)  # lift scoop

def drop_ball():
    arm_motor.run_angle(200, 90)
    wait(500)
    arm_motor.run_angle(200, -90)

def search_for_ball():
    drive_forward()
    while True:
        if ultraSS.distance() < 150:  # object detected
            stop()
            return

def go_to_goal():
    drive_forward()
    while True:
        if color_sensor.color() == Color.RED:
            stop()
            return

# MAIN LOOP
while True:
    search_for_ball()
    pick_ball()
    go_to_goal()
    drop_ball()