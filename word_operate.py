import util
import re

builtin_blacklist = ['国', '皇帝', '枪', '炮', '弹', '药', '党', '爆', '死', '杀', '屠', '兵', '暴', '灭', '军', '战', '禁', '射', '箭', '狱', '犯', '法', '毒', '囚', '侵', '流氓', '肉', '命', '恐', '反', '叛', '革', '打', '葬', '君', '斗', '亡', '黑', '刀', '刺', '封喉', '雷', '干扰', '剑', '攻', '皇', '血', '悍', '威胁', '开火', '领袖', '判', '空', '锤', '弩', '斧', '卫', '劈', '砍', '毁', '矢', '危险', '除', '行动', '罪', '魔']


class WordList(list[str]):
    def appends(self, value, message):
        if not value:
            print(f'Failed to append word: {value}: value is None')
            return
        if value in self:
            print(f'Failed to append word: {value}: value already exists')
            return

        self.append(value)
        print(f'Append word: {value}: {message}')

    def removes(self, value, message):
        self.remove(value)
        print(f'Remove word: {value}: {message}')

    def _traversal(self, hook):
        for value in self.copy():
            hook(value)

    def _remove(self, expression_func, type_):
        def remove(value):
            if expression_func(value):
                self.removes(value, '' + type_ + '匹配')
        self._traversal(remove)

    def remove_signal_word(self):
        self._remove(lambda v: len(v) == 1, '单字')

    def remove_overdose_word(self):
        self._remove(lambda v: len(v) >= 10, '字数大于等于10')

    def remove_blacklist_word(self, blacklist):
        self._remove(lambda v: re.search('|'.join(blacklist), v), '黑名单正则')

    def remove_blank(self):
        self._remove(lambda v: v.replace(' ', '') == '', '空行')

    def remove_general(self):
        self._remove(lambda v: type(v) != str, '非字符串')

    def remove_notchinese(self):
        self._remove(lambda v: not util.contains_only_chinese(v), '非纯中文')
