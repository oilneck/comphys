'''Complex matrix'''
import numpy as np

i0 = 1j

sX = np.matrix([[0,1],[1,0]])
sY = np.matrix([[0,-i0],[i0,0]])
sZ = np.matrix([[1,0],[0,-1]])

zero = np.zeros((2,2)) #全要素が0で初期化された2行2列の行列

sigma_x = np.block([[sX,zero],[zero,sX]]) # ブロック行列として並べる
sigma_y = np.block([[sY,zero],[zero,sY]])
sigma_z = np.block([[sZ,zero],[zero,sZ]])

sigma_xy = sigma_x * sigma_y
print('sigma_x * sigma_y =\n', sigma_xy, '\n')

print('i * sigma_z =\n', i0 * sigma_z, '\n')

print('{sigma_x, sigma_y}=\n', sigma_xy + sigma_y * sigma_x, '\n')
