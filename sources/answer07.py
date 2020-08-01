import matplotlib.pyplot as plt

def fibo(n):
    if n==0:
        f_p = 0
    elif n==1:
        f_p = 1
    else:
        f_p_2 = 0
        f_p_1 = 1
        for p in range(2, n+1):
            f_p = f_p_1 + f_p_2
            f_p_2 = f_p_1
            f_p_1 = f_p
    return f_p

x_list = range(1, 101)
y_list = []

for n in x_list:
    f_n = fibo(n)
    f_nn = fibo(n+1)
    ratio = f_nn / f_n
    y_list.append(ratio)

plt.plot(x_list, y_list)
plt.show()
