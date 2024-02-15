% 读取CSV文件
data = readtable('mds_coordinates_with_z.csv');

% 提取X, Y, Z坐标
X = data{:, 'XCoordinate'};
Y = data{:, 'YCoordinate'};
Z = data{:, 'ZValue'};

% 绘制3D散点图
scatter3(X, Y, Z, 'filled')
xlabel('X Coordinate')
ylabel('Y Coordinate')
zlabel('Z Value')
title('3D Scatter Plot')
hold on

% 创建拟合平滑曲面
fittedSurface = fit([X, Y], Z, 'lowess');
% 绘制拟合曲面
plot(fittedSurface, [X, Y], Z)

% 在最下方添加等高线图
zlim = get(gca, 'ZLim');  % 获取当前Z轴的限制
minZ = zlim(1);  % 获取Z轴的最小值
contourf(X, Y, Z, 20, 'LevelList', linspace(minZ, max(Z), 20))
colormap jet  % 设置等高线图的颜色映射
colorbar  % 显示颜色条

hold off
