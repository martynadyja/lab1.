from cs50 import get_int, get_float
from numpy import pi, linspace, meshgrid, sqrt, cos, exp, sin
from matplotlib.pyplot import plot, figure, show, cm
from mpl_toolkits.mplot3d import Axes3D

#0 Use alternative way of reading inputs - using library (0.5p)

x = get_int("x: ")
y = get_int("y: ")

print("-"*10)
print(x + y)
print("-"*10)

print(f"x + y: {x + y}")
print(f"x - y: {x - y}")
print(f"x * y: {x * y}")
print(f"x / y: {x / y}")
print(f"x modulo y: {x % y}")

#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)

X = get_int("radius X: ")
Y = get_int("radius Y: ")

perimeterCircle1 = 2 * pi * X
perimeterCircle2 = 2 * pi * Y
fieldCircle1 = pi * (X**2)
fieldCircle2 = pi * (Y**2)

def perimeter(r):
    if X >= 0:
        return perimeterCircle1
    if Y >= 0:
        return perimeterCircle2
if X >= 0:
    print("Perimeter for the first circle is:", perimeterCircle1)
else:
    print("Perimeter for the first circle doesn't exist.")
if Y >= 0:
    print("Perimeter for the second circle is:", perimeterCircle2)
else:
    print("Perimeter for the second circle doesn't exist.")

def field(r):
    if X >= 0:
        return fieldCircle1
    if Y >= 0:
        return fieldCircle2
if X >= 0:
    print("Field for the first circle is:", fieldCircle1)
else:
     print("Field for the first circle doesn't exist.")
if Y >= 0:
    print("Field for the second circle is:", fieldCircle2)
else:
    print("Field for the second circle doesn't exist.")

#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)

X2 = range(1, 12)
Y2 = range(1, 8)

for i in range(len(X2)):
    for j in range(len(Y2)):
        if (X2[i] % Y2[j]) == 0 and X2[i] % 2 == 0 and Y2[j] % 2 == 0:
            print("Found X is:", X2[i], "and found Y is:", Y2[j])

#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint - use the "ternary operator" as we did calculating xIsEvenLog above.
#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)

X3 = get_float("radius X: ")
Y3 = get_float("radius Y: ")

XisdivisiblebyY = X3 % Y3 == 0
Z = 'X is divisible by Y.' if XisdivisiblebyY else 'X is not divisible by Y.'
XY = round(X3 / Y3, 2)
print("X/Y is:", XY, Z)

#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)

x2_knots = linspace(-3*pi,3*pi,201)
y2_knots = linspace(-3*pi,3*pi,201)
X4, Y4 = meshgrid(x2_knots, y2_knots)
R = sqrt(X4**2+Y4**2)
Z2 = cos(R)**2*exp(-0.1*R)
ax = Axes3D(figure(figsize=(8,5)))
ax.plot_surface(X4, Y4, Z2, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
show()

x3_knots = linspace(-10.0, 10.0, 250)
y3_knots = linspace(-10.0, 10.0, 250)
X5, Y5 = meshgrid(x3_knots, y3_knots)
X6 = X5**2
Y6 = Y5**2
Z3 = X6 + Y6
ax = Axes3D(figure(figsize=(8,5)))
ax.plot_surface(X5, Y5, Z3, rstride=1, cstride=1, cmap=cm.spring, linewidth=0.4)
show()

#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5) work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)
