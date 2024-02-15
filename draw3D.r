# 设置CRAN镜像
options(repos = c(CRAN = "https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))

# 安装包
install.packages("scatterplot3d")
install.packages("plotly")

# 加载包
library(scatterplot3d)
library(plotly)


# 读取CSV文件
data <- read.csv("mds_coordinates_with_z.csv")

# 绘制3D散点图并添加标签
s3d <- scatterplot3d(data$XCoordinate, data$YCoordinate, data$ZValue, pch=20, color="blue", main="3D Scatter Plot with Labels")
text(s3d$xyz.convert(data$XCoordinate, data$YCoordinate, data$ZValue), labels=data$Label, cex=0.7, pos=4)

# 创建交互式图表
fig <- plot_ly(data, x = ~XCoordinate, y = ~YCoordinate, z = ~ZValue, type = 'scatter3d', mode = 'markers', text = ~Label, marker = list(size = 4))

# 添加拟合的平滑曲面 (可能需要根据您的数据调整)
fit <- loess(ZValue ~ XCoordinate + YCoordinate, data = data)
grid <- expand.grid(XCoordinate = seq(min(data$XCoordinate), max(data$XCoordinate), length = 30), YCoordinate = seq(min(data$YCoordinate), max(data$YCoordinate), length = 30))
grid$ZValue <- predict(fit, newdata = grid)

# 将拟合曲面添加到图表
fig <- fig %>% add_surface(x = ~grid$XCoordinate, y = ~grid$YCoordinate, z = ~grid$ZValue, opacity = 0.5)

# 添加等高线图
fig <- fig %>% add_contour(x = ~grid$XCoordinate, y = ~grid$YCoordinate, z = ~grid$ZValue, showscale = TRUE)

# 显示图表
fig
