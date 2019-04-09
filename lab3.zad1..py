#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)

from numpy import pi
from cs50 import get_int, get_float

type = input("Choose type of figure: ")

if type == "circle":
    x = get_float("radius: ")
if type == "rectangle":
    x = get_float("side1: ")
    y = get_float("side2: ")
if type == "triangle":
    x = get_float("base: ")
    y = get_float("height: ")
if type == "rhombus":
    x = get_float("diagonal1: ")
    y = get_float("diagonal2: ")

def countField():
    if type == "circle" and x >= 0:
        return pi * (x**2)

    if type == "rectangle" and x >= 0 and y >= 0:
        return x * y

    if type == "triangle" and x >= 0 and y >= 0:
        return (1/2) * x * y

    if type == "rhombus" and x >= 0 and y >= 0:
        return (x * y)/2

if type == "circle" and x >= 0:
    print("The field of a given figure is:", countField())
if type == "circle" and x < 0:
    print("The field doesn't exist.")

if type == "rectangle" and x >= 0 and y >= 0:
    print("The field of a given figure is:", countField())
if type == "rectangle" and x < 0:
    print("The field doesn't exist.")
if type == "rectangle" and y < 0:
    print("The field doesn't exist.")

if type == "triangle" and x >= 0 and y >= 0:
    print("The field of a given figure is:", countField())
if type == "triangle" and x < 0:
    print("The field doesn't exist.")
if type == "triangle" and y < 0:
    print("The field doesn't exist.")

if type == "rhombus" and x >= 0 and y >= 0:
    print("The field of a given figure is:", countField())
if type == "rhombus" and x < 0:
    print("The field doesn't exist.")
if type == "rhombus" and y < 0:
    print("The field doesn't exist.")
















