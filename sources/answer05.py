'''class5 テストの点数から成績をつけるプログラム'''

import numpy as np


score = input("Enter your score:")

assert score.isdecimal(), 'input value must be positive integer'

score = int(score)
grade = None

if   (0 <= score) & (score <= 60):
    grade = 'F'
elif (61 <= score) & (score <= 70):
    grade = 'D'
elif (71 <= score) & (score <= 80):
    grade = 'C'
elif (81 <= score) & (score <= 90):
    grade = 'B'
elif (91 <= score) & (score <= 100):
    grade = 'A'
else:
    raise Exception('The input value must be an integer between 0 and 100')

print('Your grade is {}'.format(grade))
