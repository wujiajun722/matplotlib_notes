import sympy as sp
import matplotlib.pyplot as plt
import os
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x,y = sp.symbols("x y")
expr1 = x**2  + 4*x - y - 1
expr2 = x + y + 1
eq1 = sp.Eq(expr1,0)
eq2 = sp.Eq(expr2,0)

solution = sp.solve([eq1,eq2],[x,y])
# print(solution)

fig,ax = plt.subplots()
i = 0
for s in solution:
    ax.text(0.2,0.6,f'方程${sp.latex(eq1)}$和${sp.latex(eq2)}$的解:',fontsize = 12)
    ax.text(0.4,0.5 - 0.1 * i,f'$x_{i + 1} = {sp.latex(s[0])}$和$y_{i + 1} = {sp.latex(s[1])}$',fontsize = 12)
    i += 1
    pass
# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section4/" + script_name + '.png')
plt.show()
