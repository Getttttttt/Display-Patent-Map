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
    
    print(patent_dict)
    
    if 'citation_infor' in patent_dict:
        patent_cite_number = len(patent_dict['citation_infor']) - 2
    else: patent_cite_number = 0
    if 'citedBy_infor' in patent_dict:
        citedBy_infor_number = len(patent_dict['citedBy_infor']) - 2
    else: citedBy_infor_number = 0
    if 'similar_document' in patent_dict:
        similar_document_number = len(patent_dict['similar_document']) - 1
    else: similar_document_number = 0
    if 'inventor_number' in patent_dict:
        inventor_number = int(patent_dict['inventor_number'])
    else: inventor_number = 0    
    if 'classfication_nums' in patent_dict:
        classfication_nums = int(patent_dict['classfication_nums'])
    else: classfication_nums = 0 
    if 'application_events' in patent_dict:
        application_events = len(patent_dict['application_events'])
    else: application_events = 0 
    if 'active_area' in patent_dict:
        active_area_number = len(patent_dict['active_area'])
    else: active_area_number = 0 
    if 'not_active_area' in patent_dict:
        not_active_area_number = len(patent_dict['not_active_area'])
    else: not_active_area_number = 0 
    if 'patent_application_claiming_priority' in patent_dict:
        patent_application_claiming_priority_number = len(patent_dict['patent_application_claiming_priority'])
    else: patent_application_claiming_priority_number = 0 
    if 'legal_event' in patent_dict:
        legal_event_number = len(patent_dict['legal_event'])
    else: legal_event_number = 0 
    if 'patent_priority_application' in patent_dict:
        patent_priority_application_number = len(patent_dict['patent_priority_application'])-1
    else: patent_priority_application_number = 0 
    
    output_file.write(patent_dict['ID'])
    output_file.write(',')
    output_file.write(str(citedBy_infor_number))
    output_file.write(',')
    output_file.write(str(patent_cite_number))
    output_file.write(',')
    output_file.write(str(similar_document_number))
    output_file.write(',')
    output_file.write(str(inventor_number))
    output_file.write(',')
    output_file.write(str(classfication_nums))
    output_file.write(',')
    output_file.write(str(application_events))
    output_file.write(',')
    output_file.write(str(active_area_number))
    output_file.write(',')
    output_file.write(str(not_active_area_number))
    output_file.write(',')
    output_file.write(str(patent_application_claiming_priority_number))
    output_file.write(',')
    output_file.write(str(legal_event_number))
    output_file.write(',')
    output_file.write(str(patent_priority_application_number))
    output_file.write('\n')
    

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
    with open('./networkRecord.txt', 'w',encoding='utf-8') as output_file:
        traverse_directory(root_path, process_file,output_file)