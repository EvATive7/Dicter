import os

def read_words_from_file(file_path) -> list:
    all_lines = []
    # 打开文件并逐行读取内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        all_lines.extend(lines)
    print(f"read {len(all_lines)} words from {file_path}")
    return all_lines

def read_words_from_exists() -> list:
    # 存储所有行的数组
    all_lines = []

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk('exists'):
        for file_name in files:
            if '.txt' in file_name:
                file_path = os.path.join(root, file_name)
                all_lines.extend(read_words_from_file(file_path))
    return all_lines