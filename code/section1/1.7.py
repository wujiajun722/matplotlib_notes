import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

fig, ax = plt.subplots()
x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
ax.set_title("箭头示例2")
ax.plot(x, y)
# 直箭头示例
arrow1 = mpatches.FancyArrowPatch(
    (0.7*np.pi, 1.2), (0.5 * np.pi, 1),
    arrowstyle='->', mutation_scale=20,
    connectionstyle='arc3,rad=0.3',
    color='red',
    transform=ax.transData, clip_on=False
)
arrow2 = mpatches.FancyArrowPatch(
    (3.7*np.pi, -1.2), (3.5 * np.pi, -1),
    arrowstyle='->', mutation_scale=20,
    connectionstyle='arc3,rad=0.3',
    color='red',
    transform=ax.transData, clip_on=False
)

ax.add_patch(arrow1)
ax.add_patch(arrow2)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))  # x轴位置
ax.spines['left'].set_position(('data', 0))    # y轴位置

# 添加箭头 ,clip_on=False的作用是防止箭头被裁剪掉
ax.plot(1, 0, '>r',transform=ax.get_yaxis_transform(),clip_on=False) #transform=ax.get_yaxis_transform()表示箭头在y轴上
ax.plot(0, 1, '^b', transform=ax.get_xaxis_transform(),clip_on=False)   #transform=ax.get_xaxis_transform()表示箭头在x轴上

# 点一个(π/2,1)位置
ax.plot(0.5*np.pi, 1, 'og', markersize=8)
ax.plot(3.5*np.pi, -1, 'ob', markersize=8)

# 标注文字说明
ax.text(0.7*np.pi - 0.1, 1.2 - 0.1, "最高点($\pi$/2,1)", color='red', fontsize=10)
ax.text(3.7*np.pi - 0.1, -1.2 - 0.1, "最低点(7$\pi$/2,1)", color='red', fontsize=10)

plt.savefig('figures/section1/1.7.png')  # 保存图形为文件
plt.show()