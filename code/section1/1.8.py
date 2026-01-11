import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


fig,ax = plt.subplots()
fig.suptitle("文字说明")
ax.set_title("latex文字说明")

ax.plot([0.5,1,1.5,2,2.5],[-0.5,-0.25,0,0.25,0.5],'og', markersize=2)
# 添加文字说明
ax.text(0.5, -0.5, "matplotlib可以插入latex公式", color='green', fontsize=12)
ax.text(1, -0.25, r"$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$", color='green', fontsize=15)
ax.text(1.5, 0, r"$\int_a^b f(x) \mathrm{d}x = F(b) - F(a)$", color='green', fontsize=15)
ax.text(2, 0.25, r"$e^{i \pi} + 1 = 0$", color='green', fontsize=15)
ax.text(2.5, 0.5, r"$\nabla \cdot \mathbf{E} = \frac {\rho} {\varepsilon_0}$", color='green', fontsize=15)



ax.set_xlim(0,3.5)
ax.set_ylim(-1, 1)

ax.grid(True)
plt.savefig('figures/section1/1.8.png')  # 保存图形为文件
plt.show()