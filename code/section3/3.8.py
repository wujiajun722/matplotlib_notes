import matplotlib.pyplot as plt
import numpy as np
import os
import sympy as sp

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig,ax = plt.subplots()

x,y = sp.symbols("x y")
expr1 = -x**2 - y**2 + 1
expr2 = x - sp.sin(2 * y)

eq1 = sp.Eq(expr1,0)
eq2 = sp.Eq(expr2,0)

y1 = sp.solve(eq1,y)
y2 = sp.solve(eq2,y)
# 绘制每一个解
x_vals = np.arange(-3,3,0.00001)
for i,sol in enumerate(y1):
    # print(i)
    # print(sol)
    y_func = sp.lambdify(x,sol,'numpy')
    y_vals = y_func(x_vals)
    # print(y_vals)
    ax.plot(x_vals, y_vals,color = 'purple',label = f"${sp.latex(eq1)}$")    
    pass

for i,sol in enumerate(y2):
    # print(i)
    # print(sol)
    y_func = sp.lambdify(x,sol,'numpy')
    y_vals = y_func(x_vals)
    # print(y_vals)
    ax.plot(x_vals, y_vals,label = f"${sp.latex(eq1)}$")    
    pass


plt.show()


