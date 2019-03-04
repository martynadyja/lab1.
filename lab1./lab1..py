from numpy import array, abs, exp, linspace, sin, cos, pi
from matplotlib.pyplot import plot, show, xlabel, ylabel, legend, figure, xlim, title, subplot

#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

for x in range(56, 101):
    print((2*x)**2 + 2*x + 2)


#2 ask the user for a number and print its factorial (1p)

print("Podaj liczbę: ")
x = int(input())
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
if x < 0:
    print("Factorial doesn't exist.")
elif x == 0:
    print("Factorial is 1.")
else:
    print("Factorial of", x, "is", factorial(x))


#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

x2 = array([8, 2, 9, 10, 53, 6, 7])
def y(x2):
    return (min(x2*2 - 5))
print("The lowest value of function is: ", y(x2))


#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)

x3 = [-1, -3, 6, 9, 12]
x4 = linspace(0, 4.*pi, 100)
y2 = abs(x3)
y3 = sin(x4)
print(y2)
subplot(2, 1, 1)
plot(x3, y2, 'ro', color = 'green', label = 'y2')
xlabel('x')
ylabel('y')
title("Title")
legend(loc = 'upper left', fontsize = 10)
xlim(-4, 14)
subplot(2, 1, 2)
plot(x4, y3, color = 'red', label = 'y3')
xlabel('x')
ylabel('y')
legend(loc = 'upper right', fontsize = 12)

show()
