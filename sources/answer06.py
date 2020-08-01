import numpy as np

for n in range(50, 151):
    for m in range(1, n):
        if n % m == 0:
            m0 = m
    if m0 == 1:
        print('prime num: {}'.format(n))

print('_' * 50)
# フェルマーの小定理を使った解答
def is_prime(n):
    n = int(np.abs(n))
    if n == 2: return True
    return pow(2, n-1, n) == 1

[print(n) for n in range(50, 151) if is_prime(n)]
