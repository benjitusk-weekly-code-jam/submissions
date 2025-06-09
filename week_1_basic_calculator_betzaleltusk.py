import math


def add(x, y):
    print(x + y)


def sub(x, y):
    print(x - y)


def mult(x, y):
    print(x * y)


def div(x, y):
    print(x / y)


def log(x, y):
    print(math.log(x, y))


x = float(input("X:"))
y = float(input("Y:"))

add(x, y)
sub(x, y)
mult(x, y)
div(x, y)
log(x, y)
