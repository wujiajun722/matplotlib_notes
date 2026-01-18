# 利用matplotlib.pyplot也可以直接绘制扇形饼图
import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 准备数据
labels = ['类别A', '类别B', '类别C', '类别D']
sizes = [25, 35, 20, 20]
colors = ["#ff9999","#663758","#123456","#456789"]

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制饼图并获取扇形patch
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

# 自定义每个扇形的样式
for i, wedge in enumerate(wedges):
    # 设置边框颜色和宽度
    wedge.set_edgecolor('white')
    wedge.set_linewidth(2)
    # 设置透明度
    wedge.set_alpha(0.8)

# 添加标题
ax.set_title('饼图示例', fontsize=16, fontweight='bold')

# 确保饼图是圆形
ax.axis('equal')

# 添加图例
ax.legend()

# 调整布局
plt.tight_layout()

# 文件保存
script_name = os.path.splitext(os.path.basename(__file__))[0]
plt.savefig("figures/section2/" + script_name + '.png')
plt.show()