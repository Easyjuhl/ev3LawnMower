
#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sensor.lego import TouchSensor

btn = Button()
tch = TouchSensor()
speeds = 40
ma = LargeMotor('outA')
mb = LargeMotor('outC')

cl = ColorSensor()
cl.mode='COL-AMBIENT'
while True:
    if btn.any():
        break

    ma.on(speed=speeds)
    mb.on(speed=speeds)
    if tch.is_pressed:
        speeds = 100
    
    print(cl.value())

ma.off()
mb.off()