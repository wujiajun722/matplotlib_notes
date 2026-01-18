
import sympy as sp

# 定义符号变量
x, y, z = sp.symbols('x y z')

# 定义一个包含符号的表达式
expr = x**2 + 2*y*z + 3*x - y**2

# 方法1: 使用subs()方法代入具体数值
result1 = expr.subs(x, 2)
result2 = expr.subs([(x, 2), (y, 3), (z, 1)])

# 方法2: 使用evalf()进行数值计算
result3 = expr.subs([(x, 1.5), (y, 2.0), (z, 0.5)]).evalf()

# 方法3: 一次性代入多个变量
subs_dict = {x: 1, y: 2, z: 3}
result4 = expr.subs(subs_dict)

# 输出结果
print("原始表达式:", expr)
print("代入x=2:", result1)
print("代入x=2, y=3, z=1:", result2)
print("代入x=1.5, y=2.0, z=0.5并计算:", result3)
print("代入x=1, y=2, z=3:", result4)

# 也可以使用subs()的链式调用
result5 = expr.subs(x, 1).subs(y, 2).subs(z, 3)
print("链式代入结果:", result5)
