import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

a,b,c = 1,1,1
A = [0.,0.]
# 利用余弦定理
# cosA=(b^2+c^2-a^2)/2bc
thetaA = (b**2 + c**2 - a**2) / (2*b*c)
angle_radians = np.arccos(thetaA)
# 转换为度数
angle_degrees = np.degrees(angle_radians)

print(f"{angle_degrees:.2f}")
B = [A[0] + c, A[1]]
C = [A[0] + b * np.cos(angle_radians), A[1] + b * np.sin(angle_radians)]


fig,ax = plt.subplots()
triangle = mpatches.Polygon([A, B, C], facecolor='lightblue', edgecolor='darkred', linewidth=2, alpha=0.7)
ax.add_patch(triangle)
ax.text(0.5,0.5,r"$ \cos A = \frac{b^2 + c^2 - a^2}{2bc}$",fontsize = 18)
ax.text(*A,'$A$',color = "red")
ax.text(*B,'$B$')
ax.text(*C,'$C$',color = 'blue')

ax.set_xlim(0,c + 0.1)
ax.set_ylim(0,b)
ax.set_aspect('equal')

plt.savefig("figures/section2/2.6.png")
plt.show()