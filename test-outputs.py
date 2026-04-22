from ev3dev2.motor import LargeMotor, OUTPUT_A
import time

motor = LargeMotor(OUTPUT_A)

motor.on(50)      # run at 50% speed
time.sleep(5)     # run for 5 seconds
motor.off()       # stop
