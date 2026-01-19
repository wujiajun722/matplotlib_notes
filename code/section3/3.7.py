import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig,ax = plt.subplots()

x,y = sp.symbols("x y",real = True)
expr1 = y**2-(x**2 + x + 2)
expr2 = -y + 2

eq1,eq2 = sp.Eq(expr1,0),sp.Eq(expr2,0)
results = sp.solve([eq1,eq2],[x,y])

y1 = sp.solve(eq1,y)
y2 = sp.solve(eq2,y)

# 绘制每个解
x_vals = np.linspace(-3, 3, 2000)
for i, sol in enumerate(y1):
    y_func = sp.lambdify(x, sol, 'numpy')
    y_vals = y_func(x_vals)
    ax.plot(x_vals, y_vals,color = 'purple',label = f"${sp.latex(eq1)}$")
    
for i, sol in enumerate(y2):
    # 将符号表达式转换为数值函数
    y_func = sp.lambdify(x, sol, 'numpy')
    try:
        y_vals = y_func(x_vals)
        ax.plot(x_vals, y_vals,color = 'red',
                linewidth=2,label = f"${sp.latex(eq2)}$")
    except Exception as e:
        ax.plot(x_vals, [y_vals] * len(x_vals),color = 'red',
                linewidth=2,label = f"${sp.latex(eq2)}$")
        continue

# 绘制交点
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
        
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))  # x轴位置
ax.spines['left'].set_position(('data', 0))    # y轴位置

# 添加箭头 ,clip_on=False的作用是防止箭头被裁剪掉
ax.plot(1, 0, '>r',transform=ax.get_yaxis_transform(),clip_on=False) #transform=ax.get_yaxis_transform()表示箭头在y轴上
ax.plot(0, 1, '^b', transform=ax.get_xaxis_transform(),clip_on=False)   #transform=ax.get_xaxis_transform()表示箭头在x轴上

ax.legend()
# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section3/" + script_name + '.png')
plt.show()
