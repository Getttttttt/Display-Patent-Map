import os

def read_txt(input_path):
    result_dict = {}
    current_key = None
    current_value = None

    with open(input_path, 'r',encoding='utf-8') as file:
        for line in file:

            if not line:
                continue  # 跳过空行
            if line.rstrip('\n').isdigit():
                continue
            # 检查是否为键
            if not line.startswith('    '):
                current_key = line.strip()
                result_dict[current_key] = []
            else:
                # 添加值到列表中
                result_dict[current_key].append(line.strip())

    return result_dict

def filter_strings(input_list):
    result_list = []
    
    for i in range(len(input_list)):
        current_string = input_list[i]
        
        # 如果当前字符串是最后一个字符串，或者下一个字符串是字母，将当前字符串添加到结果列表中
        if i == len(input_list) - 1 or input_list[i + 1].isalpha():
            result_list.append(current_string.replace(',', ''))
    
    return result_list

def process_file(file_path,output_file):
    # 在这里执行对文件的处理操作
    patent_dict = read_txt(file_path)
    if 'classfication_items' in patent_dict:
        cpc_list = patent_dict['classfication_items']
        cpc_list_clean = filter_strings(cpc_list)
        line_to_write = ",".join(cpc_list_clean) + "\n"
        output_file.write(line_to_write)

def traverse_directory(root_directory, process_function,output_file):
    # 遍历根目录下的所有文件夹和文件
    for root, dirs, files in os.walk(root_directory):
        # 遍历当前文件夹中的文件
        for file_name in files:
            file_path = os.path.join(root, file_name)
            process_function(file_path,output_file)

if __name__ == '__main__':
    # 示例用法
    root_path = "./"  # 请替换为实际的目录路径
    with open('./CPCRecord.txt', 'w',encoding='utf-8') as output_file:
        traverse_directory(root_path, process_file,output_file)