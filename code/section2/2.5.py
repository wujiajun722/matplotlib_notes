import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

a = 1
b = 1
theta = np.radians(60)  # 夹角60度转换为弧
A = [0.2, 0.2]
B = [A[0] + a, A[1]]
C = [A[0] + b * np.cos(theta), A[1] + b * np.sin(theta)]
A = np.array(A)
B = np.array(B)
C = np.array(C)
print(f'{A},{B},{C}')
fig,ax = plt.subplots()
ax.text(A[0],A[1],"A")
ax.text(B[0],B[1],"B")
ax.text(C[0],C[1],"C")
triangle = mpatches.Polygon([A, B, C], facecolor='lightblue', edgecolor='darkred', linewidth=2, alpha=0.7)

vec_ab = B - A
vec_ac = C - A
vec_bc = B - C
print(vec_ab)
ab = np.linalg.norm(vec_ab)
print(f'边长ab:{ab}')

mid_ab = (A + B) / 2
print(f'中点坐标:{mid_ab}')

angle_A = np.dot(vec_ab,vec_ac) / (np.linalg.norm(vec_ab) * np.linalg.norm(vec_ac))
# 计算弧度角
angle_radians = np.arccos(angle_A)
# 转换为度数
angle_degrees = np.degrees(angle_radians)
print(f"A夹角{angle_degrees}")

# 计算角平分线
# 归一化向量
unit_vec_ab = vec_ab / np.linalg.norm(vec_ab)
unit_vec_ac = vec_ac / np.linalg.norm(vec_ac)
print(unit_vec_ab)
print(unit_vec_ac)


# # 计算角平分线向量
bisector = unit_vec_ab + unit_vec_ac + A
ax.text(bisector[0],bisector[1],'角平分线')
x, y = zip(A,bisector)  # 使用zip解包坐标
print(x)
print(y)
plt.plot(x,y,'bo',linestyle = '-',label = '角平分线')

angle_A = np.dot(vec_ab,bisector) / (np.linalg.norm(vec_ab) * np.linalg.norm(bisector))
# 计算弧度角
angle_radians = np.arccos(angle_A)
# 转换为度数
angle_degrees = np.degrees(angle_radians)
print(f"A夹角{angle_degrees}")

# # 计算中线
mid_bc = (B + C) / 2
ax.text(mid_bc[0],mid_bc[1],'中点')
print(mid_bc)
x, y = zip(A, mid_bc)  # 使用zip解包坐标
# print(x)
# print(y)
plt.plot(x,y,'ro',linestyle = '-',label = '中线')


ax.add_patch(triangle)
ax.set_aspect('equal')
plt.savefig('figures/section2/2.5.png',dpi=300)
plt.show()


