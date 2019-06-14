#1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)

import numpy as np
import matplotlib.pyplot as plt

a = 1
h = 0.1
T = 3
initial_x = 1

t = np.arange(0, T, h)
x = np.zeros(t.shape)
x[0] = initial_x

for i in range(t.size - 1):
    x[i + 1] = x[i] + h * (20 * a * x[i])

plt.plot(t, x, 'o')
plt.xlabel('t', fontsize = 14)
plt.ylabel('x', fontsize = 14)
plt.show()





