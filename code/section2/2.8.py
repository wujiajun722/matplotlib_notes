import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

A = [0.,0.]
B = [1.,0.]
theta = 120
radians = np.radians(theta)

C = [A[0] + 1. * np.cos(radians),A[1] + 1. * np.sin(radians)]

fig,ax = plt.subplots()
x,y = zip(A,B)
plt.plot(x,y,'r-')
x,y = zip(A,C)
plt.plot(x,y,'r-')
# 绘制弧线,width和height是椭圆形的长边和短边,相等时相当于圆形弧线,theta1和theta2分别是起点和终点角度
arc = mpatches.Arc((0,0),width=0.3,height=0.3,angle=0,theta1=0,theta2=theta,linewidth = 2,color = "blue")

ax.add_patch(arc)
ax.text(0.1,0.1,fr'$\alpha = {theta}^o$',fontsize = 12)
ax.set_aspect('equal')
plt.savefig('figures/section2/2.8.png')
plt.show()
