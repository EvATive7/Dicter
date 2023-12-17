import util

def filter_single_word(ls:list) -> list:
    filtered = []
    for w in ls.copy():
        if len(w) == 1:
            filtered.append(w)
            ls.remove(w)
            print(f'移除单字“{w}”')
        pass
    pass

def filter_blacklist_word(ls:list) -> None:
    bl = util.read_list_from_folder('./data/ArknightsSCELCustomData/blacklist')
    for w in ls.copy():
        if w in bl:
            ls.remove(w)
            print(f'移除词汇“{w}”，命中规则（黑名单）')
    pass

def filter_sensitive_word(ls:list) -> None:
    sensitive_keywords = \
        ['国','皇帝','枪','炮','弹','药','党','爆','死','杀','屠','兵','暴','灭',
        '军','战','禁','射','箭','狱','犯','法','毒','囚','侵','流氓','肉','命',
        '恐','反','叛','革','打','葬','君','斗','亡','黑','刀','刺','封喉','雷',
        '干扰','剑','攻','皇','血','悍','威胁','开火','领袖','判','空','锤','弩',
        '斧','卫','劈','砍','毁','矢','危险','除','行动','罪','魔']
    for w in ls.copy():
        for s in sensitive_keywords:
            if s in w:
                try:
                    ls.remove(w)
                    print(f'移除词汇“{w}”，命中规则“{s}”')
                except:
                    pass
    pass

def default_filter(ls:list)->None:
    for w in ls.copy():
        if w.replace(' ','') == '':
            ls.remove(w)
            print(f'移除词汇“{w}”，命中规则（空行）')
    pass