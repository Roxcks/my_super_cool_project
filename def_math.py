from math import sin
number = int(input())
math_func = input()

def square(num):
    return num**2
def cube(num):
    return num**3
def sqr(num):
    return num**0.5
def module(num):
    return abs(num)
def sinus(num):
    return sin(num)

funcs = {
    'квадрат': square,
    'куб': cube,
    'корень': sqr,
    'модуль': module,
    'синус': sinus,
}
print(funcs[math_func](number))


