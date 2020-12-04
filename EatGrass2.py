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

state = "Onward"
SawBlack = 0

while True:

    r,g,b=cl.rgb
    Color = RGB_to_HSL.colour(r,g,b)

    if state == "Onward":
        ma.on(speed=40)
        mc.on(speed=40)

        SawBlack += 1

        if btn.any():
            break
        
        if Color == "BLACK":
            state="BackCauseBlack"
        
        if tch.is_pressed:
            state = "SPEED"
    
    elif state == "BackCauseBlack":
        ma.on(speed=-15)
        mc.on(speed=-5)
        sleep(5)
        state = "Onward"
        Sawblack=0

    elif state = "SPEED":
        ma.off()
        mc.off()
        sleep(1)
        ma.on(speed=-10)
        mc.on(speed=-10)
        sleep(1)
        ma.on(speed=100)
        mc.on(speed=100)
        sleep(5)
        state = "Onward"        