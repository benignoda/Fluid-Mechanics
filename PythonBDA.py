# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#import math
#import numpy
#import matplotlib

# Grafica x - y #
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10,0.1)
y = x*np.exp(x)

plt.clf()
plt.plot(x,y)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Figura 1')
plt.show()