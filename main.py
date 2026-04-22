from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
import time

# --------------------
# MOTORS
# --------------------
left_motor = LargeMotor('ev3-ports:outA')
right_motor = LargeMotor('ev3-ports:outB')
arm_motor = LargeMotor('ev3-ports:outC')

# --------------------
# SENSORS
# --------------------
ultra = UltrasonicSensor(INPUT_1)
color = ColorSensor(INPUT_2)

# --------------------
# MOVEMENT
# --------------------
def drive(speed=40):
    left_motor.on(speed)
    right_motor.on(speed)

def stop():
    left_motor.off()
    right_motor.off()

# --------------------
# ARM
# --------------------
def pick_ball():
    arm_motor.on_for_degrees(30, 90)
    time.sleep(0.5)
    arm_motor.on_for_degrees(30, -90)

def drop_ball():
    arm_motor.on_for_degrees(30, 90)
    time.sleep(0.5)
    arm_motor.on_for_degrees(30, -90)

# --------------------
# LOGIC
# --------------------
def search_ball():
    drive(40)
    while True:
        if ultra.distance_centimeters < 15:
            stop()
            return
        time.sleep(0.05)

def go_to_goal():
    drive(40)
    while True:
        if color.color == ColorSensor.COLOR_RED:
            stop()
            return
        time.sleep(0.05)

# --------------------
# MAIN LOOP
# --------------------
while True:
    search_ball()
    pick_ball()
    go_to_goal()
    drop_ball()
