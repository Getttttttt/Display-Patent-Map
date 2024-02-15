
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

if __name__ == '__main__':
    patent = read_txt('./EP001/EP2077424A3.txt')
    print(patent)