import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
fig = plt.figure("title")             # an empty figure with no Axes
fig, ax = plt.subplots()       # a figure with a single Axes
fig.suptitle("Figure title")  # set the Figure title
ax.set_title("Axes title")    # set the Axes title
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
axs[0, 0].set_title("Axes [0,0] title")  # set the title for a specific Axes
axs[1, 1].set_title("Axes [1,1] title")
fig.tight_layout()  # adjust spacing between subplots

# a figure with one Axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
axs['left'].set_title("左侧子图标题")
axs['right_top'].set_title("右上子图标题")
axs['right_bottom'].set_title("右下子图标题") 
fig.tight_layout()  # adjust spacing between subplots
plt.savefig('figures/section1/1.4.png')  # 保存图形为文件
plt.show()
