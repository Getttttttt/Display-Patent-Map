import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.pyplot as plt

import csv
from collections import Counter
import math


definitions_list = [
    "B60L7/10", "B60T1/10", "D21F5/20", "F01K17/02", "F01K17/06", "F01K27/02", "F02C7/10",
    "F02G5/00", "F15B21/14", "F16D61/00", "F17C9/04", "F22B1/16", "F22B1/18", "F22D1/40",
    "F22G1/02", "F22G1/12", "F22G5/06", "F23G5/46", "F24F3/147", "F24F12/00", "F24H8/00",
    "F27D17/00", "F28C1/08"
]

cited_by = [80232, 63011, 749, 7333, 5182, 9054, 10206, 8631, 41461, 29970, 18330, 4448, 12867, 279, 1717, 304, 40, 22090, 10543, 5528, 13971, 3842, 280]

def read_txt_file(file_path):
    result_list = []

    with open(file_path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            elements = line.split(',')
            result_list.append(elements)

    return result_list

def flatten_and_remove_duplicates(input_list):
    result_set = set()

    for sublist in input_list:
        for element in sublist:
            result_set.add(element)

    result_list = list(result_set)
    return result_list


# 示例用法
file_path = 'CPCRecord.txt'  # 请替换为实际的文件路径
output_file_path = 'output_adjacency_matrix.csv'  # 输出 CSV 文件路径

two_dimension_list = read_txt_file(file_path)
one_dimension_list = flatten_and_remove_duplicates(two_dimension_list)

# 计算二维矩阵的大小
matrix_size = len(definitions_list)
# 创建二维矩阵，每个元素初始化为0
goal_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

for single_list in two_dimension_list:
    for element1 in single_list:
        for element2 in single_list:
            if (element1 in definitions_list) and (element2 in definitions_list):
                goal_matrix[definitions_list.index(element1)][definitions_list.index(element2)] += 1

convert_matrix = []
for i in goal_matrix:
    convert_matrix.append([])
    for j in i:
        convert_matrix[-1].append(-j+681)
        

# 使用MDS算法进行降维
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=42)
result = mds.fit_transform(convert_matrix)

print(result)

# 将2D坐标映射到5x5的方向区域
mapped_points = np.floor(result * 5)  # 映射到整数坐标

# 将结果和Z值写入CSV文件
with open('mds_coordinates_with_z.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 写入列标题
    writer.writerow(['Label', 'X Coordinate', 'Y Coordinate', 'Z Value'])

    # 遍历结果和标签列表，写入数据
    for label, coordinates, z_value in zip(definitions_list, mapped_points, cited_by):
        writer.writerow([label, coordinates[0], coordinates[1], z_value])



# 绘制结果
plt.scatter(mapped_points[:, 0], mapped_points[:, 1])

# 标记数据点
for i, txt in enumerate(definitions_list):
    plt.annotate(txt, (mapped_points[i, 0], mapped_points[i, 1]))

plt.show()
