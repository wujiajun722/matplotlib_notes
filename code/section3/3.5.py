import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig,ax = plt.subplots()
ax.set_title('圆锥曲线的一般方程')
A,B,C,D,E,F,x,y = sp.symbols('A,B,C,D,E,F,x,y')
expr = A*x**2 + B * x * y + C * y**2 +D * x + E * y + F
eq = sp.Eq(expr,0)
# 如果圆锥曲线在原点,则没有x和y的一次项,也就是D和E为0
subs_dict = {A:-3,B:4,C:-4,D:0,E:0,F:4}
result = eq.subs(subs_dict)

# 解出y关于x的表达式
solutions = sp.solve(result, y)

print(sp.latex(solutions))

# 绘制每个解
x_vals = np.linspace(-10, 10, 2000)
for i, sol in enumerate(solutions):
    # 将符号表达式转换为数值函数
    y_func = sp.lambdify(x, sol, 'numpy')
    
    try:
        y_vals = y_func(x_vals)
        # 只绘制实数部分
        mask = np.isreal(y_vals)
        if np.any(mask):
            ax.plot(x_vals[mask], np.real(y_vals[mask]),color = 'red',
                    label=f'解 {i+1}', linewidth=2)
    except Exception as e:
        print(f"绘制解 {i+1} 时出错: {e}")
        continue

ax.text(0.,0.,f'${sp.latex(result)}$',
        bbox={'boxstyle': 'round', 
              'facecolor': 'lightblue',
              'alpha': 0.7,
              'pad': 0.5}
        ,alpha = 0.8)

offset_x = 0.5  # x方向的偏移量（向左为负）
offset_y = 0.5  # y方向的偏移量（向下为负）
text_x = ax.get_xlim()[0] + offset_x  # 获取x轴最小值并加上偏移量
text_y = ax.get_ylim()[0] + offset_y  # 获取y轴最小值并加上偏移量

ax.text(text_x,text_y,f'$y={sp.latex(solutions[0])}$',fontsize = 12)
ax.text(text_x,text_y + offset_y,f'$y={sp.latex(solutions[1])}$',fontsize = 12)

# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section3/" + script_name + '.png')
plt.show()