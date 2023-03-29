#!/usr/bin/env python3

import time
from telemetrix import telemetrix

#arduino pin numbers
servo = 12
motor = 10

#motor commands
forward = 110
stop = 90
backward = 75

#servo commands
left = 85
center = 93
right = 105

board = telemetrix.Telemetrix()
board.set_pin_mode_servo(servo)
board.set_pin_mode_servo(motor)

#board.servo_write(servo, servo command)
#board.servo_write(motor, forward)
time.sleep(2)



#function to move forward for a amount of time

def forward():
  board.servo_write(motor, forward)
