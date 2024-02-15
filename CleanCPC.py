def filter_strings(input_list):
    result_list = []
    
    for i in range(len(input_list)):
        current_string = input_list[i]
        
        # 如果当前字符串是最后一个字符串，或者下一个字符串是字母，将当前字符串添加到结果列表中
        if i == len(input_list) - 1 or input_list[i + 1].isalpha():
            result_list.append(current_string.replace(',', ''))
    
    return result_list

# 示例用法
input_strings = ['F', 'F,2,4', 'F,2,4,F', 'F,2,4,F,3,/,0,0', 'F,2,4,F,3,/,1,2', 'F,2,4,F,3,/,1,4', 'F', 'F,2,4', 'F,2,4,F', 'F,2,4,F,1,2,/,0,0', 'F,2,4,F,1,2,/,0,0,1', 'F,2,4,F,1,2,/,0,0,2', 'F', 'F,2,4', 'F,2,4,F', 'F,2,4,F,3,/,0,0', 'F,2,4,F,3,/,1,2', 'F,2,4,F,3,/,1,4', 'F,2,4,F,3,/,1,5,3', 'Y', 'Y,0,2', 'Y,0,2,B', 'Y,0,2,B,3,0,/,0,0', 'Y,0,2,B,3,0,/,5,6']
filtered_strings = filter_strings(input_strings)
print(filtered_strings)
