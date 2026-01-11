import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False
# 创建子图
fig,ax = plt.subplots(3,2,figsize=(10,15))

# angle=0表示不旋转,facecolor表示填充颜色,edgecolor表示边框颜色,linewidth表示边框宽度,alpha表示透明度
rect = mpatches.Rectangle((0.2,0.2),0.6,0.6,angle=0,facecolor="lightblue",edgecolor="blue",linewidth=2,alpha=0.7)
ax[0,0].add_patch(rect)
ax[0,0].set_xlim(0,1)
ax[0,0].set_ylim(0,1)
# adjustable参数设置为box时，长宽比固定
ax[0,0].set_aspect('equal', adjustable='box')

# angle=45表示旋转45度,默认是绕着左下角旋转
rect = mpatches.Rectangle((0.2,0.2),0.6,0.6,angle=45,facecolor="lightgreen",edgecolor="green",linewidth=2,alpha=0.7)
ax[0,1].add_patch(rect)
ax[0,1].set_xlim(0,1)
ax[0,1].set_ylim(0,1)
ax[0,1].set_aspect('equal', adjustable='box')

# 填充颜色和边框颜色,填充无颜色,边框填充红色
rect = mpatches.Rectangle((0.2,0.2),0.6,0.6,angle=0,facecolor='none',edgecolor="red",linewidth= 2,alpha=1)
ax[1,0].add_patch(rect)
ax[1,0].set_xlim(0,1)
ax[1,0].set_ylim(0,1)
ax[1,0].set_aspect('equal', adjustable='box')
# 修改长方形的位置在原点,默认是以左下角为原点
rect = mpatches.Rectangle((0,0),0.6,0.6,angle=0,facecolor="orange",edgecolor="brown",linewidth=2,alpha=0.7)
ax[1,1].add_patch(rect)
ax[1,1].set_xlim(0,1)
ax[1,1].set_ylim(0,1)
ax[1,1].set_aspect('equal', adjustable='box')
ax[1,1].plot(0,0,'ro',markersize = 10) # 标记原点位置

# 修改长方形的长和宽,宽为1,长为0.6
rect = mpatches.Rectangle((0.0,0.1),1,0.6,angle=0,facecolor="purple",edgecolor="none",linewidth=2,alpha=0.7)
ax[2,0].add_patch(rect)
ax[2,0].set_xlim(0,1)
ax[2,0].set_ylim(0,1)
ax[2,0].set_aspect('equal', adjustable='box')

# 修改长方形的透明度,alpha=0.3表示透明度为30%
rect1 = mpatches.Rectangle((0.2,0.2),0.6,0.6,angle=0,facecolor="red",edgecolor="none",linewidth=2,alpha=0.3)
rect2 = mpatches.Rectangle((0.3,0.3),0.6,0.6,angle=0,facecolor="blue",edgecolor="none",linewidth=2,alpha=0.4)
ax[2,1].add_patch(rect1)
ax[2,1].add_patch(rect2)
ax[2,1].set_xlim(0,1)
ax[2,1].set_ylim(0,1)
ax[2,1].set_aspect('equal', adjustable='box')

plt.savefig("figures/section2/2.2.png",dpi=300)
plt.show()