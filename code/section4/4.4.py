import sympy as sp
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig,ax = plt.subplots()

x,y = sp.symbols("x y",real = True)
a,b,c = sp.symbols("a b c",real = True)
expr = a*x**2 + b*x + c - y
eq = sp.Eq(expr,0)
eq = eq.subs({y:0})
solutions = sp.solve(eq,x)
print(solutions)

i = 0
for solution in solutions:
    plt.text(0.5,0.5 - 0.2*i,f"$x_{i + 1} = {sp.latex(solution)}$",fontsize = 12)
    i += 1
    pass
plt.text(0.5,0.8,"$ax^2 + bx + c = 0$解",fontsize = 15)
# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section4/" + script_name + '.png')
plt.show()

