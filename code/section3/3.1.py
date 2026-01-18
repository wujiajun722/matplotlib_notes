import numpy as np
import matplotlib.pyplot as plt
import os

# 设置中文字体，例如使用“SimHei”
plt.rcParams['font.sans-serif'] = ['SimHei']  # 添加'SimHei'到字体列表
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为□的问题
fig,ax = plt.subplots()
fig.suptitle(r'隐函数$\frac{x^2}{4} + \frac{y^2}{1} = 1$')
# 定义x和y的范围
x = np.linspace(-3,3, 100)
y = np.linspace(-1.5,1.5, 100)
X, Y = np.meshgrid(x, y)
 
# 计算Z值，Z = x^2/4 + y^2/1 - 1
Z = X**2/4 + Y**2/1 - 1

# 绘制等高线图
ax.contour(X, Y, Z, levels=[0], colors='black')
ax.plot(1,0, '>r',transform=ax.get_yaxis_transform(),clip_on=False) #transform=ax.get_yaxis_transform()表示箭头在x轴上
ax.plot(0,1, '^b',transform=ax.get_xaxis_transform(),clip_on=False) #transform=ax.get_yaxis_transform()表示箭头在y轴上
ax.set_aspect(1)
ax.set_title(r'隐函数$\frac{x^2}{4} + \frac{y^2}{1} = 1$')


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
#改变坐标轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section3/" + script_name + '.png')
plt.show()
