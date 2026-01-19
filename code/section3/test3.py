
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 8))

x, y = sp.symbols("x y", real=True)
expr1 = y - (x**2 + x + 1)
expr2 = y - 5 - x

eq1, eq2 = sp.Eq(expr1, 0), sp.Eq(expr2, 0)
results = sp.solve([eq1, eq2], [x, y])

y1 = sp.solve(eq1, y)
y2 = sp.solve(eq2, y)

# 绘制每个解
x_vals = np.linspace(-5, 5, 2000)
for i, sol in enumerate(y1):
    y_func = sp.lambdify(x, sol, 'numpy')
    y_vals = y_func(x_vals)
    ax.plot(x_vals, y_vals, color='purple', linewidth=2, label=f'$y = x + x + 1$')
    
for i, sol in enumerate(y2):
    # 将符号表达式转换为数值函数
    y_func = sp.lambdify(x, sol, 'numpy')
    try:
        y_vals = y_func(x_vals)
        ax.plot(x_vals, y_vals,color = 'red',
                linewidth=2)
    except Exception as e:
        ax.plot(x_vals, [y_vals] * len(x_vals),color = 'red',
                linewidth=2)
        continue


# 绘制交点
if results:
    for point in results:
        x_coord, y_coord = point
        ax.plot(x_coord, y_coord, 'ro', markersize=8)
        ax.annotate(f'({x_coord:.2f}, {y_coord:.2f})', 
                   (x_coord, y_coord), 
                   xytext=(10, 10), 
                   textcoords='offset points',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                   fontsize=10)

ax.grid(True, alpha=0.3)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('二次函数与水平直线的交点', fontsize=14)
ax.legend()
# 绘制一条横线和一条竖线
ax.axhline(y=0, color='k', linewidth=2)
ax.axvline(x=0, color='k', linewidth=2)

plt.tight_layout()
plt.show()
