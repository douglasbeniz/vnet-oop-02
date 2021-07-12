#!/usr/bin/python3

"""
source https://runestone.academy/runestone/books/published/thinkcspy/Inheritance/02-IntroToInheritance.html
"""

class Point:
    """ Class base """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


class LabeledPointInherit(Point):
    """ Class inheriting from base one """
    def __init__(self, initX, initY, label):
        self.x = initX
        self.y = initY
        self.label = label

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + " (" + self.label + ")"


class LabeledPointExtend(Point):
    """ Class extending the base one """
    def __init__(self, initX, initY, label):
        super().__init__(initX, initY)
        self.label = label

    def __str__(self):
        return super().__str__() + " (" + self.label + ")"


# -----------------------------------------------------------------------------
# Objects
# -----------------------------------------------------------------------------
p = Point(7.35, 6.81)
print(p)

labeledPt1 = LabeledPointInherit(4.9,3.2,"Here")
print(labeledPt1)

labeledPt2 = LabeledPointExtend(1.25,6.05,"There")
print(labeledPt2)
