import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体，例如使用“SimHei”
plt.rcParams['font.sans-serif'] = ['SimHei']  # 添加'SimHei'到字体列表
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为□的问题


if __name__ == "__main__":
    x, y = sp.symbols('x y')
    
    # 椭圆的一般方程示例: 2x² + 3y² + 4x - 6y - 5 = 0
    # 这里我们构造一个标准椭圆方程并转换为一般形式
    # 标准椭圆: (x+1)²/4 + (y-1)²/3 = 1
    # 展开后: 3(x+1)² + 4(y-1)² = 12
    # 一般形式: 3x² + 6x + 3 + 4y² - 8y + 4 = 12
    # 最终: 3x² + 4y² + 6x - 8y - 5 = 0
    
    equation = 3*x**2 + 4*y**2 + 6*x - 8*y - 5
    
    print("椭圆一般方程:", equation, "= 0")
    
    # 将方程转换为标准形式验证
    # 3x² + 6x + 4y² - 8y = 5
    # 3(x² + 2x) + 4(y² - 2y) = 5
    # 3(x+1)² - 3 + 4(y-1)² - 4 = 5
    # 3(x+1)² + 4(y-1)² = 12
    # (x+1)²/4 + (y-1)²/3 = 1
    
    # 解出y关于x的表达式
    solutions = sp.solve(equation, y)
    
    # 创建绘图
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # 绘制每个解
    x_vals = np.linspace(-4, 2, 2000)
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
    
    # 标注中心点
    center_x, center_y = -1, 1
    ax.plot(center_x, center_y, 'ro', markersize=8, label='中心点(-1, 1)')
    
    # 标注长轴和短轴端点
    # 长半轴a = 2 (x方向), 短半轴b = √3 ≈ 1.73 (y方向)
    a = 2
    b = np.sqrt(3)
    
    # 长轴端点
    ax.plot([center_x - a, center_x + a], [center_y, center_y], 
            'b--', alpha=0.7, label='长轴')
    # 短轴端点
    ax.plot([center_x, center_x], [center_y - b, center_y + b], 
            'g--', alpha=0.7, label='短轴')
    
    # 设置图形属性
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('椭圆一般方程: $3x^2 + 4y^2 + 6x - 8y - 5 = 0$', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_aspect('equal')
    
    # 设置坐标轴范围
    ax.set_xlim(-4, 2)
    ax.set_ylim(-1.5, 3.5)
    
    plt.tight_layout()
    plt.show()
    
    # 验证几个点是否满足方程
    print("\n验证点是否在椭圆上:")
    test_points = [(-1, 1), (-3, 1), (1, 1), (-1, 1+np.sqrt(3)), (-1, 1-np.sqrt(3))]
    for point in test_points:
        x_val, y_val = point
        result = equation.subs([(x, x_val), (y, y_val)])
        print(f"点({x_val}, {y_val}): {result} = 0")
