import sympy as sp
import matplotlib.pyplot as plt
import os
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = sp.symbols("x")
expr = x**2  + 4*x - 1
eq = sp.Eq(expr,0)

solution = sp.solve(eq,x)
print(solution)

fig,ax = plt.subplots()
i = 0
for s in solution:
    ax.text(0.4,0.6,f'方程${sp.latex(eq)}$的解:',fontsize = 12)
    ax.text(0.5,0.5 - 0.2 * i,f'$x_{i + 1} = {sp.latex(s)}$',fontsize = 12)
    i += 1
# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section4/" + script_name + '.png')
plt.show()
