'''Monte carlo method'''

import random
import math

Nmax = int(1e6)
count = 0
for _ in range(Nmax):
    x = random.random()
    y = random.random()
    z = random.random()
    t = random.random()
    rr = x ** 2 + y ** 2 + z ** 2 + t ** 2

    if rr <= 1:
        count += 1

v4d = count * 2 ** 4 / Nmax # 2^4の因子を忘れずに
v4d_exac = math.pi ** 2 / 2

print("v4d=", v4d)
print("v4d_exac=", v4d_exac)
