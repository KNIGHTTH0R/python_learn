from decimal import getcontext, Decimal
from math import pi
from fractions import Fraction

print("0.1 + 0.2 = {}".format(0.1+0.2))

print("0.1 + 0.4 = {}".format(0.1+0.4))

print("1/10 = {}".format(1/10))

print("Is (0.1 + 0.1 + 0.1 == 0.3) ?")

print(0.1 + 0.1 + 0.1 == 0.3)

print("Is (0.1 + 0.1 + 0.1 == 0.3) ?")

print(round(0.1 + 0.1 + 0.1, 5) == round(0.3, 5))

print(round(10.33333, 3))

#Decimal

print(getcontext())

getcontext().prec = 5

print(Decimal(1)/Decimal(3))

getcontext().prec = 30

print(Decimal(pi))

#Fraction

num1 = Fraction(2,3)
num2 = Fraction(1,3)

print("num1 = {} and num2 = {}".format(num1,num2))

print(num1 + num2)

print(num1 - num2)

print(num1*10)

print(num1/num2)

print(type(num1))