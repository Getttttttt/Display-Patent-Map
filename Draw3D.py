import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
import pandas as pd

# 读取数据
data = pd.read_csv('mds_coordinates_with_z.csv')
X = data['X Coordinate']
Y = data['Y Coordinate']
Z = data['Z Value']  # 假设CSV文件中的Z列已经更名为"Quality"
labels = data['Label']

# 创建网格来绘制曲面
xi = np.linspace(min(X), max(X), 100)
yi = np.linspace(min(Y), max(Y), 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((X, Y), Z, (xi, yi), method='cubic')

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(xi, yi, zi, cmap='coolwarm', alpha=0.6)

# 绘制散点图
scat = ax.scatter(X, Y, Z, color='black')

# 标注
for i, txt in enumerate(labels):
    ax.text(X[i], Y[i], Z[i], txt, size=7)

# 添加等高线图
ax.contourf(xi, yi, zi, zdir='z', offset=min(Z)-20, cmap='coolwarm', alpha=0.3)

# 设置标签和标题
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Quality')
ax.set_title('3D Scatter Plot with Fitted Surface and Contours')

# 显示图形
plt.show()
