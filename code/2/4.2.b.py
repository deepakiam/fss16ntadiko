#!/usr/bin/python
"""Think Like a Scientist: Excerise 4.3

"""
from __future__ import division
from swampy.TurtleWorld import *
import math

world =  TurtleWorld()
bob = Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def petal(t,r,angle):
    arc(bob,r,angle)
    lt(t, 180-angle)
    arc(bob,r,angle)
    lt(t,180-angle)

def flower(t,r,n, angle):
	for i in range(n):
		petal(t,r,angle)
		lt(bob,360/n)
	

bob.delay=0.00000001

flower(bob,100,10,60)
wait_for_user()