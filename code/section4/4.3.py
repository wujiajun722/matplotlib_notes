import sympy as sp
import matplotlib.pyplot as plt
import os

x,y,a,b = sp.symbols("x y a b")
expr = a*x + b - y
eq = sp.Eq(expr,0)

solution = sp.solve(eq,x)
print(solution)

result = eq.subs({a:1,b:2,y:0})
print(result)
solution = sp.solve(result,x)
print(solution)