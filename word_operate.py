import util
def filter_single_word(ls:list) -> list:
    filtered = []
    for w in ls.copy():
        if len(w) == 1:
            filtered.append(w)
            ls.remove(w)
        pass
    pass

def filter_blacklist_word(ls:list) -> None:
    bl = util.read_list_from_folder('blacklist')
    for w in ls.copy():
        if w in bl:
            ls.remove(w)
    pass

def filter_sensitive_word(ls:list) -> None:
    sensitive_keywords = ['国','皇帝','枪','炮','弹','药','党','爆','死','杀','屠','士兵','暴','灭',
                          '军','战','禁','射','箭','狱','犯','法','毒','囚','侵','流氓','肉','命']
    for w in ls.copy():
        for s in sensitive_keywords:
            if s in w:
                try:
                    ls.remove(w)
                except:
                    pass
    pass