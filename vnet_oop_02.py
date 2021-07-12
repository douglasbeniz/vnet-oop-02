#!/usr/bin/python3

"""
source https://runestone.academy/runestone/books/published/thinkcspy/Inheritance/02-IntroToInheritance.html
"""

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

p = Point(7, 6)
print(p)
