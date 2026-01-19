
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 定义符号变量
x = sp.Symbol('x',complex = True)

# 1. 解三角方程
print("1. 三角方程求解:")
eq1 = sp.Eq(sp.sin(x), 1/2)
solutions1 = sp.solve(eq1, x, domain=sp.Interval(-4*sp.pi, 2*sp.pi))
print(f"sin(x) = 1/2 在 [0, 2π] 范围内的解: {solutions1}")

# 2. 解反三角方程
print("\n2. 反三角方程求解:")
eq2 = sp.Eq(sp.asin(x), sp.pi/6)
solutions2 = sp.solve(eq2, x)
print(f"asin(x) = π/6 的解: {solutions2}")

# 3. 解包含反三角函数的方程
print("\n3. 包含反三角函数的方程:")
eq3 = sp.Eq(sp.sin(sp.acos(x)), 1/2)
solutions3 = sp.solve(eq3, x, domain=sp.Interval(-5, 5))
print(f"sin(acos(x)) = 1/2 的解: {solutions3}")

# 4. 解三角方程组
print("\n4. 三角方程组求解:")
y = sp.Symbol('y', real=True)
eq4_1 = sp.Eq(sp.sin(x) + sp.cos(y), 1)
eq4_2 = sp.Eq(sp.sin(x) - sp.cos(y), 0)
solutions4 = sp.solve([eq4_1, eq4_2], [x, y], domain=sp.Reals)
print(f"方程组解: {solutions4}")

# 5. 数值验证
print("\n5. 数值验证:")
if solutions1:
    for sol in solutions1:
        numeric_val = sol.evalf()
        print(f"x = {numeric_val} 时, sin(x) = {sp.sin(numeric_val).evalf()}")

