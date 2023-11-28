from util import read_list_from_folder,write_list_to_file,get_formatted_datetime,pinyin_sort
import word_operate
import gamedata

words = []
words.extend(read_list_from_folder('exists'))
gamedata.get_all(words)
pinyin_sort(words)

output_type = ['desktop','m','t'][0] #输出版本

if (output_type == 'desktop'):
    write_list_to_file(f'{get_formatted_datetime()}',words)

if (output_type == 'm'):
    #手机版搜狗需要
    word_operate.filter_single_word(words) 
    word_operate.filter_blacklist_word(words)
    word_operate.filter_sensitive_word(words)
    write_list_to_file(f'{get_formatted_datetime()}',words,1999)

if (output_type == 't'):
    pass
