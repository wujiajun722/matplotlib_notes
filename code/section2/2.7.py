import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 初始条件
thetaA,thetaB = 30,90
c = 1
A = [0.,0.]

thetaC = 180 - thetaA - thetaB
if thetaC < 0:
    print("构造不了三角形")
    pass

angle_radiansA = np.radians(thetaA)
angle_radiansB = np.radians(thetaB)
angle_radiansC = np.radians(thetaC)

a = np.sin(angle_radiansA) / (np.sin(angle_radiansC) / c)
b = np.sin(angle_radiansB) / (np.sin(angle_radiansC) / c)

print(f"{a},{b}")

B = [A[0] + c, A[1]]
C = [A[0] + b * np.cos(angle_radiansA), A[1] + b * np.sin(angle_radiansA)]

fig,ax = plt.subplots()
triangle = mpatches.Polygon([A, B, C], facecolor='lightblue', edgecolor='darkred', linewidth=2, alpha=0.7)
ax.add_patch(triangle)
ax.set_xlim(0,c + 0.1)
ax.set_ylim(0,b)
ax.text(0.5,0.3,r"$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$",fontsize = 18)
ax.text(*A,'$A$',color = "red")
ax.text(*B,'$B$')
ax.text(*C,'$C$',color = 'blue')
ax.set_aspect('equal')
plt.savefig("figures/section2/2.7.png")
plt.show()