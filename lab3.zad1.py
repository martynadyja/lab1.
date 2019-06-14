#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)

from numpy import pi

figure = ['circle', 3]

def fieldoffigure(figure):
    if figure[0] == 'circle' and len(figure) == 2:
        return (figure[1]) ** 2 * pi

    if figure[0] == 'rectangle' and len(figure) == 3:
        return figure[1] * figure[2]

    if figure[0] == 'triangle' and len(figure) == 3:
        return (1 / 2) * figure[1] * figure[2]

    if figure[0] == 'rhombus' and len(figure) == 3:
        return (figure[1] * figure[2]) / 2

if len(figure) == 0:
    print("Wrong number of arguments.")

elif fieldoffigure(figure) == None:
    print("Wrong number of arguments.")

elif fieldoffigure(figure):
    print("The field of a given figure is:", fieldoffigure(figure))
