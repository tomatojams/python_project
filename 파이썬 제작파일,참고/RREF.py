from typing import Optional, Any, Final

import numpy as np
from fractions import Fraction

matrixinitial = np.array(
    [[1.0, 2.0, 3, 1.0], [0.0, 2.0, -4.0, 6.0], [2.0, 4.0, -6.0, 14.0]]
)

global matrix
matrix = matrixinitial
global pivot


def exchange(i, j):  # 두행을 바꾸는 함수입니다.
    global matrix
    LineA = matrix[i - 1].copy()  # 카피를 써줘야 오류가 안남
    matrix[i - 1] = matrix[j - 1]
    matrix[j - 1] = LineA
    print(matrix, "\n")


def make_pivot(i, j):  # 피봇을 찾고 1로 만든후 피봇을 찾았다고 표식을 합니다.
    global matrix
    global pivot
    if matrix[i - 1, j - 1] == 1:
        pivot = True  # 피봇을 찾았다고 표식을 해요.
        if i != j:
            exchange(i, j)  # 피봇 위치가 맞지 않으면 맞도록 위치를 바꿉니다.
    elif matrix[i - 1, j - 1] != 0:  # 현재값이 0이 아닐때만
        tempcoef = matrix[i - 1, j - 1]
        matrix[i - 1] = matrix[i - 1] / tempcoef  # 피봇을 1로 만듭니다.
        pivot = True  # 피봇을 찾았다고 표식을 해요.
        print(matrix, "\n")
        if i != j:
            exchange(i, j)  # 피봇 위치가 맞지 않으면 맞도록 위치를 바꿉니다.


def make_zeros(i, n):  # 피봇 위아래를 0으로 만듭니다.
    coef = -(matrix[n - 1, i - 1] / matrix[i - 1, i - 1])
    matrix[n - 1] = matrix[n - 1] + (coef * matrix[i - 1])
    print(matrix, "\n")


def make_zero1(i):  # 대충 짰어요. 피봇 위아래로 0으로 만드는 함수를 부릅니다.
    if i == 1:
        make_zeros(1, 2)
        make_zeros(1, 3)
    elif i == 2:
        make_zeros(2, 1)
        make_zeros(2, 3)
    elif i == 3:
        make_zeros(3, 1)
        make_zeros(3, 2)


pivot = False
print("문제")
print(matrixinitial)
print("\n풀이과정")

# 메인프로그램입니다. 함수 두개로 끝 헤헤
for i in range(1, 4):
    pivot = False
    for j in range(1, 4):
        if pivot == False and i <= j:
            make_pivot(i, j)
            if pivot == True:
                make_zero1(i)

print("\nx1={},x2={},x3={}".format(matrix[0, 3], matrix[1, 3], matrix[2, 3]))
