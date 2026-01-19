import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig,ax = plt.subplots()

x,y = sp.symbols("x y")
expr1 = x + y + 1
expr2 = x**2  +  y**2 + 3*x + 4*y 

eq1,eq2 = sp.Eq(expr1,0),sp.Eq(expr2,0)
results = sp.solve([eq1,eq2],[x,y])

y1 = sp.solve(eq1,y)
y2 = sp.solve(eq2,y)

# 绘制每个解
x_vals = np.linspace(-5, 5, 2000)
for i, sol in enumerate(y1):
    y_func = sp.lambdify(x, sol, 'numpy')
    y_vals = y_func(x_vals)
    ax.plot(x_vals, y_vals,color = 'purple')
    

for i, sol in enumerate(y2):
    y_func = sp.lambdify(x, sol, 'numpy')
    y_vals = y_func(x_vals)
    ax.plot(x_vals, y_vals,color = 'blue')
    

# 寻找交点
for result in results:
    plt.plot(*result,'ro')

# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section3/" + script_name + '.png')
plt.show()