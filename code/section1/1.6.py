import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

# 弯箭头示例
arrow = mpatches.FancyArrowPatch(
    # 起点和终点坐标
    (0.2, 0.2), (.8, .8),
    # 箭头样式和属性
    arrowstyle='->,head_length=0.4,head_width=0.2',
    connectionstyle='arc3,rad=0.3',  # 弯曲半径
    # 其他属性,箭头颜色,线宽,大小等
    color='blue', linewidth=2, mutation_scale=20,
    # 坐标系是data坐标系,不裁剪
    transform=ax.transData, clip_on=False
)
ax.add_patch(arrow)

plt.savefig('figures/section1/1.6.png')  # 保存图形为文件
plt.show()

