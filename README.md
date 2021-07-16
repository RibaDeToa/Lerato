import matplotlib.pyplot as plt
import numpy as np

def f(theta):
    return 1 - (((2 * 1.5) * np.sin(theta))/ 2.7)

def derivative(f, x):
    dx = 1E-8
    return (f(x + dx) - f(x)) / dx

def x_next(f, x_n):
    return 1 - (f(x_n) / derivative(f, x_n))

def newtons_method(f, x_n = 1, i = 0, max_iter = 100):
    i = i + 1
    if (i == max_iter):
        return None
    x_n = x_next(f, x_n)
    if (abs(f(x_n)) < 1E-4):
        return x_n
    print("i:",i,"x_n:",x_n,"f(x_n)",f(x_n))
    newtons_method(f, x_n, i, max_iter)

print(newtons_method(f))
