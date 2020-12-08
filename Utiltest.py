#!/usr/bin/env micropython

from time import sleep
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sensor.lego import TouchSensor
from utils import RGB_to_HSL

btn = Button()
tch = TouchSensor()
ma = LargeMotor('outA')
mc = LargeMotor('outC')

cl = ColorSensor()
cl.calibrate_white()
while True:
    r,g,b=cl.rgb
    print(RGB_to_HSL.colour(r,g,b))

    if btn.any():
        break