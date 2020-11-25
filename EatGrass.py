#!/usr/bin/env micropython

from time import sleep
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sensor.lego import TouchSensor

btn = Button()
tch = TouchSensor()
ma = LargeMotor('outA')
mc = LargeMotor('outC')

cl = ColorSensor()
cl.calibrate_white()

state = "Onward"
Sawblack = 0

while Sawblack < 300:

    r,g,b=cl.rgb

    print("Red: {}, Green: {}, Blue: {}".format(r,g,b))
    print("State: ", state)

    if state == "Onward":
        ma.on(speed=15)
        mc.on(speed=15)

        Sawblack += 1

        if btn.any():
            break
        
        if r < 100 and g < 100 and b < 100:
            state = "GoBack"
            Sawblack = 0
        
        if tch.is_pressed:
            state = "SPEED"
    
    elif state == "SPEED":
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

    elif state == "GoBack":
        ma.on(speed=-15)
        mc.on(speed=-5)
        sleep(5)
        state = "Onward"

ma.off()
mc.off()