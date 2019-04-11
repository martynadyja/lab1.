#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'

from numpy import pi

figure1 = ['circle', 83987654567, 1]
figure2 = ['triangle', 1000, 1]

def fieldoffigure(figure):
    if figure[0] == 'circle' and len(figure) == 2:
        return figure[1]**2 * pi

    if figure[0] == 'rectangle' and len(figure) == 3:
        return figure[1] * figure[2]

    if figure[0] == 'triangle' and len(figure) == 3:
        return (1/2) * figure[1] * figure[2]

    if figure[0] == 'rhombus' and len(figure) == 3:
        return (figure[1] * figure[2])/2

def comparefigures(figure1, figure2):
    if fieldoffigure(figure1) > fieldoffigure(figure2):
        return figure1[0]
    if fieldoffigure(figure1) < fieldoffigure(figure2):
        return figure2[0]
    if fieldoffigure(figure1) == fieldoffigure(figure2):
        return 0

if len(figure1) == 0 or len(figure2) == 0:
    print("Wrong number of arguments.")

elif fieldoffigure(figure1) == None or fieldoffigure(figure2) == None:
    print("Wrong number of arguments.")

elif comparefigures(figure1, figure2) == figure1[0]:
    print("The field of the first figure", comparefigures(figure1, figure2), "has larger field.")

elif comparefigures(figure1, figure2) == figure2[0]:
    print("The field of the second figure", comparefigures(figure1, figure2), "has larger field.")

elif comparefigures(figure1, figure2) == 0:
    print("Figures are equal.")
