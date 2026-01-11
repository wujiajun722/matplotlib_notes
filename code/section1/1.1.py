import matplotlib.pyplot as plt
import numpy as np
# 创建数据
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

# 绘制图形
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('sin')

plt.savefig('figures/section1/1.1.png')  # 保存图形为文件
# Show the plot
plt.show()
