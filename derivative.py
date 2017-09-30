from sympy import *
import math
x=Symbol("x")
print(diff(sin(x**2)*x,x))
print(diff(1/(1+x**2),x))
