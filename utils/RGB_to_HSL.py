# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:36:03 2020

@author: Albert
"""
def rgbConvert(r,g,b):
    colours = [r/255.0,g/255.0,b/255.0]
    xmax = max(colours)
    xmin = min(colours)
    c = xmax-xmin
    if c == 0:
        return 0
    elif xmax == colours[2]:
        h = 60*(4+(colours[0]-colours[1])/(c))
    elif xmax == colours[1]:
        h =  60*(2+(colours[2]-colours[1])/(c))
    elif xmax == colours[0]:
        h = 60*((colours[1]-colours[2])/(c))
    if h < 0:
        return h + 360
    else:
        return h
"""
for r in range(0,255):
    for g in range(0,255):
        for b in range(0,255):
            if rgbConvert(r,g,b) > 360:
                print("Red: " + str(r) + " Green: " + str(g) + " Blue: " + str(b))
  """              