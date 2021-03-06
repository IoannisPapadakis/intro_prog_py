#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:58:26 2018

@author: christoph
"""
import numpy as np

a = np.array([1.5,2,3])
b = np.array([[1.5,2,3], [4,5,6]])


import matplotlib.pyplot as plt
# see  https://matplotlib.org/1.2.1/examples/pylab_examples/
x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)

plt.plot(x, f)
plt.ylabel('sin(x)')
plt.title("A wave")
plt.show()
