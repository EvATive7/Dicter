from util import write_list_to_file, get_formatted_datetime, pinyin_sort
import word_operate
import gamedata
import argparse

output_types = ['desktop', 'mobile_open', 'test']

parser = argparse.ArgumentParser()
parser.add_argument('output_type', choices=output_types)
args = parser.parse_args()

output_type = args.output_type

words = []
load_logs = []
removed_logs = []

load_logs += word_operate.load_exists(words)
removed_logs += word_operate.filter_blank_row(words)

if (output_type == 'desktop'):
    load_logs += gamedata.append_all(words, ['act', 'char', 'charm', 'crisis', 'enemy', 'gacha', 'term', 'item', 'rogue', 'skill', 'skin', 'stage', 'sub_prof'])
    removed_logs += word_operate.filter_overdose_word(words)
    pinyin_sort(words)
    write_list_to_file(f'{get_formatted_datetime()}', words)

if (output_type == 'mobile_open'):
    gamedata.append_all(words, ['act', 'char', 'gacha', 'term', 'skill', 'skin', 'sub_prof'])
    pinyin_sort(words)
    removed_logs += word_operate.filter_single_word(words)
    removed_logs += word_operate.filter_blacklist_word(words)
    removed_logs += word_operate.filter_sensitive_word(words)
    removed_logs += word_operate.filter_overdose_word(words)
    write_list_to_file(f'{get_formatted_datetime()}', words, 1999)

if (output_type == 'test'):
    pass

for removed_log in removed_logs:
    print(f"{removed_log['word']}被移除，命中规则：{removed_log['conclusion']}")

exit()