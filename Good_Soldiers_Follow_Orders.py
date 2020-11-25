#!/usr/bin/env micropython

from time import sleep
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sensor.lego import TouchSensor

#Which way to turn
turnway = 1
sawBlack = 0
btn = Button()
tch = TouchSensor()
ma = LargeMotor('outA')
mb = LargeMotor('outC')

cl = ColorSensor()
cl.mode='COL-REFLECT'
cl.calibrate_white()
while True:
    if btn.any():
        break
    
    if cl.reflected_light_intensity < 20:
        sawBlack = 1
    
    if sawBlack == 1 and cl.reflected_light_intensity > 20:
        turnway *= -1
        sawBlack = 0
    print(cl.reflected_light_intensity)
    sleep(0.2)
    if turnway == 1:
        ma.on(speed = 0)
        mb.on(speed = 10)
    else:
        ma.on(speed = 10)
        mb.on(speed = 0)

ma.off()
mb.off()
