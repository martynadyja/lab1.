#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'

from numpy import pi

figure1 = ['rectangle', 1, 4]
figure2 = ['circle', 1]

def FieldOfFigure(figure):
    if figure[0] == 'circle' and len(figure) == 2:
        return figure[1]**2 * pi

    if figure[0] == 'rectangle' and len(figure) == 3:
        return figure[1] * figure[2]

    if figure[0] == 'triangle' and len(figure) == 3:
        return (1/2) * figure[1] * figure[2]

    if figure[0] == 'rhombus' and len(figure) == 3:
        return (figure[1] * figure[2])/2

def CompareFigures(figure1, figure2):
    if FieldOfFigure(figure1) > FieldOfFigure(figure2):
        return FieldOfFigure(figure1)
    if FieldOfFigure(figure1) < FieldOfFigure(figure2):
        return FieldOfFigure(figure2)
    if FieldOfFigure(figure1) == FieldOfFigure(figure2):
        return FieldOfFigure(figure1) and FieldOfFigure(figure2)

if FieldOfFigure(figure1) == None and FieldOfFigure(figure2) == None:
    print('Wrong number of parameters for figure1 and for figure2.')
elif FieldOfFigure(figure1) == None:
    print('Wrong number of parameters for figure1.')
elif FieldOfFigure(figure2) == None:
    print('Wrong number of parameters for figure2.')
elif FieldOfFigure(figure1) > FieldOfFigure(figure2):
    print('The first figure', figure1[0], 'has larger field.')
elif FieldOfFigure(figure1) < FieldOfFigure(figure2):
    print('The second figure', figure2[0], 'has larger field.')
elif FieldOfFigure(figure1) == FieldOfFigure(figure2):
    print('Figures are equal.')

