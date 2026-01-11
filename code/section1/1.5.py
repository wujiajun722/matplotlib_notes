import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

fig,ax = plt.subplots()
x = np.arange(0, 4*np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y)
# 设置坐标轴标签
ax.set_xlabel("X轴标签")
ax.set_ylabel("Y轴标签")
# 设置坐标轴范围
ax.set_xlim(0, 9)
ax.set_ylim(-1, 1)
# 设置刻度
ax.set_xticks([0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi, 2.5*np.pi,3*np.pi,3.5*np.pi,4*np.pi])    
ax.set_yticks([-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])

# 设置刻度标签
# ax.set_xticklabels(['0', '零点五π', 'π', '一点五π', '2π', '二点五π','3π','三点五π','4π'])
# ax.set_yticklabels(['-1', '-0.8', '-0.6', '-0.4', '-0.2', '0', '0.2 ', '0.4', '0.6', '0.8', '1'])
# 设置标题
ax.set_title("坐标轴示例")
# 显示网格
ax.grid(True)
# 上下左右边框可见性
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# 设置刻度方向、长度、宽度和颜色
ax.tick_params(direction='inout', length=10, width=10, colors='red')
# 设置刻度线位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置刻度线样式
# 打开次刻度线
# 关闭次刻度线
ax.minorticks_off()
# 显示主次网格线
ax.grid(which='minor', linestyle='--', linewidth=0.5)
ax.minorticks_on()
ax.xaxis.set_tick_params(which='major', size=10, width=1, direction='out',colors='blue')
ax.xaxis.set_tick_params(which='minor', size=5, width=1, direction='out',colors='red')
ax.yaxis.set_tick_params(which='major', size=10, width=0.5, direction='out')
ax.yaxis.set_tick_params(which='minor', size=5, width=1, direction='in',colors='green')

# 设置坐标轴0位置
ax.spines['bottom'].set_position(('data', 0))  # x轴位置
ax.spines['left'].set_position(('data', 0))    # y轴位置

# 添加箭头 ,clip_on=False的作用是防止箭头被裁剪掉
ax.plot(1, 0, '>r',transform=ax.get_yaxis_transform(),clip_on=False) #transform=ax.get_yaxis_transform()表示箭头在y轴上
ax.plot(0, 1, '^b', transform=ax.get_xaxis_transform(),clip_on=False)   #transform=ax.get_xaxis_transform()表示箭头在x轴上

plt.savefig('figures/section1/1.5.png')  # 保存图形为文件
plt.show()