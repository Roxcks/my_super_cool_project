from fractions import Fraction

n = int(input())
a = Fraction(0, 1)

for i in range(1, n + 1):
    a += Fraction(1, i**2)

print(a)