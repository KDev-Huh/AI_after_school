# 경사하강법 코드(1변수)

# 미분 함수
def df(f, x, h=1e-4):
    return (f(x + h) - f(x - h)) / (2 * h)
# 1e-4 = 10^-4 = 0.0001

def gd(f, x0, lr, epochs):
    x = x0
    for _ in range(epochs):
        print(x)
        x = x - lr * df(f, x)
    return x


def f(x):
    return x ** 2-2*x

# print(gd(f, 3, 0.1, 100))


# 경사하강법 코드(2변수)
# 편미분 함수
def df2d(f, x, y, h=1e-4):
    return (f(x + h, y) - f(x - h, y)) / (2 * h), (f(x, y + h) - f(x, y - h)) / (2 * h)

def gd2d(f, x0, y0, lr, epochs):
    x = x0
    y = y0
    for _ in range(epochs):
        print(x, y)
        x = x - lr * df2d(f, x, y)[0]
        y = y - lr * df2d(f, x, y)[1]

    return x, y

def f2d(x, y):
    return x ** 2 + y ** 2

# print(gd2d(f2d, 3, 4, 0.2, 100))


# 선형회귀 (최소제곱오차 이용)
import numpy as np

table = {
    "x" : [5, 10, 15, 20],
    "y" : [16, 23, 31, 50]
}
xdata = np.array(table["x"])
ydata = np.array(table["y"])
# y = ax + b를 찾아내라

# 최소 제곱 오차 함수
# (yi-(axi+b))^2의 평균
def error(a, b):
    return np.mean((ydata - (a * xdata + b)) ** 2)

a = 1.5
b = 11

a, b = gd2d(error, a, b, 0.001, 10000)
print("y =", a, "x +", b)
print("error =", error(a, b))