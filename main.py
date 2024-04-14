from util import *
from provider import *

from word_operate import WordList, builtin_blacklist

config = read_yaml('data/config.yaml')
output_type = config['output_type']

words = WordList()

for provider, provider_config in config['provider'].items():
    for word in globals()[provider](provider_config).get():
        words.appends(word, f'{provider}')

blacklist = []
for _blacklist in config['blacklist']:
    if _blacklist == 'builtin':
        blacklist.extend(builtin_blacklist)
    else:
        blacklist.extend(read_list_from_file(_blacklist))

words.remove_general()
words.remove_blank()
words.remove_notchinese()
words.remove_overdose_word()

if (output_type == 'sogou_desktop'):
    pinyin_sort(words)
    write_list_to_file(f'{get_formatted_datetime()}', words)

if (output_type == 'mobile_open'):
    words.remove_signal_word()
    words.remove_blacklist_word(blacklist)

    pinyin_sort(words)
    write_list_to_file(f'{get_formatted_datetime()}', words, 1999)
