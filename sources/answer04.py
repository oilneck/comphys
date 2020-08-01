import numpy as np


A = np.matrix([[1,-1],[1,1]])
B = np.matrix([[0.5, 0.5],[-0.5, 0.5]])
C = A * B

print("A=\n", A)
print("\nB=\n", B)
print("\nC=A.B\n", C)


# 別解
'''
numpyのarray配列を用いてもよい
逆行列はnumpy線形代数パッケージ(linalg)の関数(inv)を用いる
'''
A = np.array([[1,-1],[1,1]])
B = np.linalg.inv(A)

# 行列積はnumpyのdot関数を用いる or '@'演算子を用いる

C1 = np.dot(A,B)
C2 = A.dot(B)
C3 = A @ B


print("_"*20)
print("A=\n", A)
print("\nB=\n", B)
print("\nC1=A.B=\n", C1)
print("\nC2=\n", C2)
print("\nC3=\n", C3)
