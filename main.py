from util import read_list_from_exists,write_list_to_file,get_formatted_datetime,pinyin_sort
import gamedata

words = []
words.extend(read_list_from_exists())
gamedata.get_all(words)
pinyin_sort(words)



write_list_to_file(f'output/{get_formatted_datetime()}.txt',words)

pass