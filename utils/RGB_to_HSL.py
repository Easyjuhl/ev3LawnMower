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
    l = (float(xmax)+float(xmin))/2.0
    
    if c == 0:
        return (0,l)
    elif xmax == colours[2]:
        h = 60*(4+(colours[0]-colours[1])/(c))
    elif xmax == colours[1]:
        h =  60*(2+(colours[2]-colours[1])/(c))
    elif xmax == colours[0]:
        h = 60*((colours[1]-colours[2])/(c))
    if h < 0:
        return (h + 360,l)
    else:
        return (h,l)
    
def colour(r,g,b):
       h,l = rgbConvert(r,g,b)
       if l < 0.15:
           return "BLACK"
       elif  0.9 < l:
           return "WHITE"
       elif  0 <= h and h <= 45:
           return "RED"
       elif 45 < h and h <= 75:
           return "YELLOW"
       elif 75 < h and h <= 160:
           return "GREEN"
       elif 160 < h and h <= 200:
           return "CYAN"
       elif 200 < h and h <= 280:
           return "BLUE"
       elif 280 < h and h <= 320:
           return "PURPLE"
       else:
           return "RED"
