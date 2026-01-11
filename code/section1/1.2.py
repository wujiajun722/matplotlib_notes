import matplotlib.pyplot as plt
import numpy as np
# 创建数据
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

# 绘制图形
plt.plot(x, y)
plt.xlabel('X轴标签', fontproperties='SimHei')  # 设置X轴标签为中文
plt.ylabel('Y轴标签', fontproperties='SimHei')  # 设置Y轴标签为中文
plt.title('图形标题', fontproperties='SimHei')  # 设置图形标题为中文

plt.savefig('figures/section1/1.2.png')  # 保存图形为文件
# Show the plot
plt.show()
