#3 Find a differential equation which represents a process / model (your choice) and implement it using odeint python function (1p)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

v0 = [0.1, 0, 20]

s = 10
r = 28
b = 8/3

t_min = 0
t_max = 20
h = 0.01
t = np.arange(t_min, t_max, h)

def F(x, t):
    dx = [0, 0, 0]
    dx[0] = s * (x[1] - x[0])
    dx[1] = r * x[0] - x[2] * x[0] - x[1]
    dx[2] = x[0] * x[1] - b * x[2]
    return dx

X = odeint(F, v0, t)

x1 = X[:, 0]
x2 = X[:, 1]
x3 = X[:, 2]

plt.figure(1)
plt.plot(t, x1, color = 'r')
plt.plot(t, x2, color = 'b')
plt.plot(t, x3, color = 'g')
plt.xlabel('time', fontsize = 12)
plt.ylabel('x', fontsize = 12)
plt.legend(('x1', 'x2', 'x3'), loc = 'upper right', fontsize = 12)

plt.figure(2)
plt.plot(x1, x2, color = 'r', label = 'x1-x2')
plt.xlabel('x1', fontsize = 12)
plt.ylabel('x2', fontsize = 12)
plt.legend(loc = 'upper right', fontsize = 12)


plt.show()
