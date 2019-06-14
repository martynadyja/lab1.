#5 Create your own 3d function with multiple local optima.
# Create an algorithm which takes an initial point and looks for the closest local optimum (1p)
# Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)
# If your solution is heuristic test its quality. Measure the probability of finding the GLOBAL optimum (1p).
# You can, for example, execute your search function multiple times and check if the returned result is what you expected.
# Measure the success / total trials rate (2p).

from scipy import linspace, cos, exp, random, meshgrid, zeros
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
from numpy import sin, cos, exp, argmax, max
from mpl_toolkits.mplot3d import Axes3D
import time

def f(x):
    return sin(x[0]) + cos((x[0]/3) + 1)

def neg_f(x):
    return -f(x)

def value_and_count(list):
    Value_list = []
    Count_list = []
    for x in list:
        if x not in Value_list:
            Value_list.append(x)
            Count_list.append(1)
        else:
            Count_list[Value_list.index(x)] += 1
    return Value_list, Count_list

Xmin_list = []

currenttime = time.perf_counter()

while time.perf_counter() - currenttime < 30:
    x_0 = random.randn(2)*20 - 10
    x_min = fmin(neg_f, x_0)
    Xmin_list.append([round(x_min[0], 2), round(x_min[1], 2)])

Val_list, count_list = value_and_count(Xmin_list)

probab = 0
for i in Val_list:
    print("point:", i, "value:", round(f(i), 2), "probability:", round(count_list[Val_list.index(i)]/sum(count_list) * 100, 4))
    if probab <= count_list[Val_list.index(i)]/sum(count_list) * 100:
        best_point = i
        probab = count_list[Val_list.index(i)]/sum(count_list) * 100

print("best point:", best_point, probab)

delta = 10
x_knots = linspace(best_point[0] - delta, best_point[0] + delta, 41)
y_knots = linspace(best_point[1] - delta, best_point[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(figure(figsize = (8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride = 1, cmap = cm.coolwarm, linewidth = 0.4)
ax.plot([x_0[0]], [x_0[1]], [f(x_0)], color = 'g', marker = 'o', markersize = 5, label = 'initial')
ax.plot([best_point[0]], [best_point[1]], [f(best_point)], color = 'k', marker = 'o', markersize = 5, label = 'final')
ax.legend()
show()










