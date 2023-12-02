from util import read_list_from_folder,write_list_to_file,get_formatted_datetime,pinyin_sort
import word_operate
import gamedata

words = []
exists = read_list_from_folder('exists')
print(f'从列表中读取了{len(exists)}个词：')
for index,i in enumerate(exists):
    print(f'[{index}] {i}')
words.extend(exists)

output_type = ['desktop','m_open','t','m_self'][1] #输出版本

if (output_type == 'desktop'):
    gamedata.append_all(words,['act','char','charm','crisis','enemy','gacha','term','item','rogue','skill','skin','stage','sub_prof'])
    pinyin_sort(words)
    write_list_to_file(f'{get_formatted_datetime()}',words)

if (output_type == 'm_open'):
    gamedata.append_all(words,['act','char','gacha','term','skill','skin','sub_prof'])
    pinyin_sort(words)
    #手机版搜狗需要
    word_operate.filter_single_word(words) 
    word_operate.filter_blacklist_word(words)
    word_operate.filter_sensitive_word(words)
    write_list_to_file(f'{get_formatted_datetime()}',words,1999)

if (output_type == 'm_self'):
    gamedata.append_all(words,['act','char','charm','crisis','enemy','gacha','term','item','rogue','skill','skin','stage','sub_prof'])
    pinyin_sort(words)
    word_operate.filter_single_word(words) 
    write_list_to_file(f'{get_formatted_datetime()}',words,1999)

if (output_type == 't'):
    pass
