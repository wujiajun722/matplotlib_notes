import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots()

# 定义符号变量
x = sp.symbols("x",real = True)
y = sp.symbols("y",real = True)

# 定义方程 eq2: x - sin(2*y) = 0
eq2 = sp.Eq(x - y**3 + 1, 0)

# 求解方程得到y的表达式
y_solutions = sp.solve(eq2, y)

print("原方程:", eq2)
print("求解结果:", y_solutions)
print("解的个数:", len(y_solutions))

# 验证解的正确性
for i, sol in enumerate(y_solutions):
    print(f"解{i+1}: y = {sol}")
    # 验证解是否满足原方程
    verification = eq2.lhs.subs(y, sol).simplify()
    print(f"验证: {verification} = 0")
    print()


x_vals = np.arange(-10,10,0.01)
for i,sol in enumerate(y_solutions):
    # print(i)
    # print(sol)
    y_func = sp.lambdify(x,sol,'numpy')
    y_vals = y_func(x_vals)
    # print(y_vals)
    ax.plot(x_vals, y_vals,label = f"${sp.latex(y_solutions)}$")    
    pass


plt.show()