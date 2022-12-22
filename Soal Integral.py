
"""
integration_with_scipy.py
calculates the integral of a sine function
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plotlib

x_start = 0
x_stop = 1
x_steps_interval = 0.01

x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = 4*x_values*np.exp(np.sin(x_values**2)) + np.cos(np.log(x_values))

plotlib.plot(x_values, y_values)

integration_function = lambda x: 2*x**2*np.exp(np.sin(x**2)) + np.cos(np.log(x))

integral, error = integrate.quad(integration_function, x_start, x_stop)

print("Integral Value:")
print(integral)
print("Integration Error:")
print(error)

plotlib.xlabel('x')
plotlib.ylabel('y')
plotlib.show()
