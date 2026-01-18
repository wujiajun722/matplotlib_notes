import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x,y,m,n = sp.symbols("x,y,m,n")
expr1 = m*x**2 + n*y**2
eq1 = sp.Eq(expr1,1)
eq2 = sp.Eq(y,x + 1)
eq3 = sp.Eq(2*(n - 1)/(m + n) - 2 * n / (m-n) + 1,0)

solution = sp.solve([eq1,eq2],)
print(solution)