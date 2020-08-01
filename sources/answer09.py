import numpy as np

# datファイルに書き出す
numList = [35, 11, 5, 93, 254, 23, 1001]
fout = open("input01.dat", "wt")
for num in numList:
    fout.write(str(num) + "\n")
fout.close() # この1文は忘れないように


# ------- 解答 ----------

fin = open("input01.dat", "rt")
numbers = []
for line in fin:
    numbers.append(int(line))

num_sum = sum(numbers)
num_ave = num_sum / len(numbers)

print('sum = ', num_sum)
print('average = ', num_ave)
