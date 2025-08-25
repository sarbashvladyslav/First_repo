import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import random as rand
from scipy import interpolate
from scipy import integrate

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]

time = np.linspace(0, 11, 12)

more_data = np.linspace(0, 11, 10000)
"""f_cub = interpolate.interp1d(time, speed, kind='cubic')
plt.plot(more_data, f_cub(more_data))
plt.xlim(0, 11)
plt.ylim(0, 130)
plt.grid()
result = integrate.quad(f_cub, 0, 11)
print(result)"""

f_quad = interpolate.interp1d(time, speed, kind='quadratic')
plt.plot(more_data, f_quad(more_data))
plt.xlim(0, 11)
plt.ylim(0, 130)
plt.grid()
result = integrate.quad(f_quad, 0, 11)
print(result)

plt.show()