import math
from scipy import integrate

def func(x):
    return math.sqrt(1 - x ** 2)

integ, err = integrate.quad(func, 0, 1)
num_pi = 4 * integ

print("pi= ", num_pi)
print("math.pi= ", math.pi)
