#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'

from numpy import pi
from cs50 import get_int, get_float

type1 = 'circle'
type2 = 'triangle'

setsofparameters = [[type1, 0, 9], [type2, 9, 9]]

if type1 == 'circle':
    x1 = setsofparameters[0][1]

if type2 == 'circle':
    x2 = setsofparameters[1][1]

if type1 == 'rectangle' or type1 == 'triangle' or type1 == 'rhombus':
    x1 = setsofparameters[0][1]
    y1 = setsofparameters[0][2]

if type2 == 'rectangle' or type2 == 'triangle' or type2 == 'rhombus':
    x2 = setsofparameters[1][1]
    y2 = setsofparameters[1][2]

def fieldofthefirstfigure():
    if type1 == 'circle' and x1 >= 0:
        return pi * (x1**2)

    if type1 == 'rectangle' and x1 >= 0 and y1 >= 0:
        return x1 * y1

    if type1 == 'triangle' and x1 >= 0 and y1 >= 0:
        return (1/2) * x1 * y1

    if type1 == 'rhombus' and x1 >= 0 and y1 >= 0:
        return (x1 * y1)/2

def fieldofthesecondfigure():
    if type2 == 'circle' and x2 >= 0:
        return pi * (x2**2)

    if type2 == 'rectangle' and x2 >= 0 and y2 >= 0:
        return x2 * y2

    if type2 == 'triangle' and x2 >= 0 and y2 >= 0:
        return (1/2) * x2 * y2

    if type2 == 'rhombus' and x2 >= 0 and y2 >= 0:
        return (x2 * y2)/2


if fieldofthefirstfigure() > fieldofthesecondfigure():
    print("The first figure", type1, "has larger field.")

if fieldofthefirstfigure() < fieldofthesecondfigure():
    print("The second figure", type2, "has larger field.")

if fieldofthefirstfigure() == fieldofthesecondfigure():
    print("Figures are equal.")


