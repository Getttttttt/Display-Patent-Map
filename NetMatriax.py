import csv
from collections import Counter
import csv


definitions_list = [
    "B60L7/10", "B60T1/10", "D21F5/20", "F01K17/02", "F01K17/06", "F01K27/02", "F02C7/10",
    "F02G5/00", "F15B21/14", "F16D61/00", "F17C9/04", "F22B1/16", "F22B1/18", "F22D1/40",
    "F22G1/02", "F22G1/12", "F22G5/06", "F23G5/46", "F24F3/147", "F24F12/00", "F24H8/00",
    "F27D17/00", "F28C1/08"
]


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

# 打印二维矩阵
for row in goal_matrix:
    print(row)


def write_to_csv(output_file_path, one_dimensional_list, two_dimensional_list):
    with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)

        # 写入一维列表
        csv_writer.writerow(one_dimensional_list)

        # 逐行写入二维列表
        csv_writer.writerows(two_dimensional_list)

output_file_path = 'output.csv'

write_to_csv(output_file_path, definitions_list, goal_matrix)

    
print(len(one_dimension_list))