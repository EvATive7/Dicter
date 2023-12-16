from util import read_list_from_folder,write_list_to_file,get_formatted_datetime,pinyin_sort
import word_operate
import gamedata

words = []
exists = read_list_from_folder('./data/ArknightsSCELCustomData/exists')
print(f'从列表中读取了{len(exists)}个词：')
for index,i in enumerate(exists):
    print(f'[{index}] {i}')
words.extend(exists)

word_operate.default_filter(words)

output_type = ['desktop','mobile_open','test'][0] #输出版本

if (output_type == 'desktop'):
    gamedata.append_all(words,['act','char','charm','crisis','enemy','gacha','term','item','rogue','skill','skin','stage','sub_prof'])
    pinyin_sort(words)
    write_list_to_file(f'{get_formatted_datetime()}',words)

if (output_type == 'mobile_open'):
    gamedata.append_all(words,['act','char','gacha','term','skill','skin','sub_prof'])
    pinyin_sort(words)
    #手机版搜狗需要
    word_operate.filter_single_word(words) 
    word_operate.filter_blacklist_word(words)
    word_operate.filter_sensitive_word(words)
    write_list_to_file(f'{get_formatted_datetime()}',words,1999)

if (output_type == 'test'):
    pass
