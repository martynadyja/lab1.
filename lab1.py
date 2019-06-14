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

TAB = [11, 12, 13, 14, 15, 6, 5, 1, 1]
minimal = min(TAB)
indicesOfMinimal = []

for i in range (0, len(TAB)):
    if TAB[i] == minimal:
        indicesOfMinimal.append(i)
print(minimal, indicesOfMinimal)

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)


x3 = linspace(-100, 100)
x4 = linspace(0, pi*5, 100)
y2 = exp(x3 + 2*x3)
y3 = cos(x4) + sin(x4*2)
subplot(2, 1, 1)
for i in range(len(x3)):
    plot(x3, y2, color = 'green')
xlabel('x')
ylabel('y')
title("Title")
subplot(2, 1, 2)
for i in range(len(x4)):
    plot(x4, y3, color = 'red')
xlabel('x')
ylabel('y')

show()
