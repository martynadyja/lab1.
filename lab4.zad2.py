#2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)
#2 Hint: use small step value. Use plt.legend to explain which series is the 'ideal'

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 2
h = 0.02
T = 5

initial_x = 1

t = np.arange(0, T, h)
x = np.zeros(t.shape)
x[0] = initial_x

t_ideal = np.arange(0, T, 0.001)
x_ideal = np.zeros(t_ideal.shape)
x_ideal[0] = initial_x

for i in range(t.size - 1):
    x[i + 1] = x[i] + h * (a * x[i])

for i in range(t_ideal.size - 1):
    x_ideal[i+1] = x_ideal[i] + 0.001 * (a * x_ideal[i])

plt.plot(t, x, 'o', t_ideal, x_ideal, 'g')
plt.legend(['Euler Method','Ideal solution'])
plt.xlabel('t', fontsize=14)
plt.ylabel('x', fontsize=14)
plt.show()


