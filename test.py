# main.py (EV3)
import socket
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1

motor_left = LargeMotor(OUTPUT_A)
motor_right = LargeMotor(OUTPUT_B)
us = UltrasonicSensor(INPUT_1)

HOST = ''
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")
conn, addr = server.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024).decode().strip()

    if not data:
        continue

    print("Command:", data)

    if data == "forward":
        motor_left.on(30)
        motor_right.on(30)

    elif data == "left":
        motor_left.on(-20)
        motor_right.on(20)

    elif data == "right":
        motor_left.on(20)
        motor_right.on(-20)

    elif data == "stop":
        motor_left.off()
        motor_right.off()

    # Sensor safety stop
    if us.distance_centimeters < 10:
        print("Obstacle detected → stopping")
        motor_left.off()
        motor_right.off()
