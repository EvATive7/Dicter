import os
import json
import re
from datetime import datetime
from pypinyin import lazy_pinyin

def pinyin_sort(lis):
    lis.sort(key=lambda i: lazy_pinyin(i)[0][0])

def get_formatted_datetime():
    # 获取当前日期和时间
    current_datetime = datetime.now()

    # 格式化日期和时间为字符串，类似于20231121234239
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

    return formatted_datetime

def read_words_from_file(file_path) -> list:
    all_lines = []
    # 打开文件并逐行读取内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines() if not line.startswith('#')]
        all_lines.extend(lines)
    print(f"read {len(all_lines)} words from {file_path}")
    return all_lines

def read_list_from_folder(dir) -> list:
    try:
        # 存储所有行的数组
        all_lines = []

        # 遍历文件夹中的所有文件
        for root, dirs, files in os.walk(dir):
            for file_name in files:
                if '.txt' in file_name and not file_name.startswith('#'):
                    file_path = os.path.join(root, file_name)
                    all_lines.extend(read_words_from_file(file_path))
        return all_lines
    except:
        return []
    
def read_json_file(file_path):
    # 打开 JSON 文件并加载数据
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def split_text_by_symbols(text):
    try:
        # 使用正则表达式将非字母数字字符作为分隔符进行截断
        parts = re.split(r'\W+', text)
        return parts
    except:
        return []

def contains_only_chinese(text):
    # 使用正则表达式匹配只包含中文字符的情况
    chinese_pattern = re.compile(r'^[\u4e00-\u9fa5]+$')
    return bool(re.match(chinese_pattern, text))

def split_list(input_list, chunk_size):
    """
    将输入列表按照指定的块大小进行分割
    :param input_list: 待分割的列表
    :param chunk_size: 分割后每个子列表的大小
    :return: 分割后的子列表
    """
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]


def write_list_to_file(name, content_list,split_limit = None):
    if not split_limit:
        lists = [content_list]
    else:
        lists = split_list(content_list,split_limit)
    
    if len(lists) == 1:
        multils = False
    else:
        multils = True

    for i,ls in enumerate(lists):
        # 打开文件，'w'表示写入模式，会删除原有内容
        index_str = f'_{i}' if multils else ''
        with open(f"output/{name}{index_str}.txt", 'w', encoding='utf-8') as file:
            print("向文件写入：")
            # 将列表的每个元素写入文件，每个元素占一行
            for item in ls:
                file.write(str(item) + '\n')
                print(item,end='，')