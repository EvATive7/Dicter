import util

exists_folder = './data/ArknightsSCELCustomData/exists'
sensitive_folder = './data/ArknightsSCELCustomData/sensitive'


class WordReason:
    EXISTS = "EXISTS"
    GAMEDATA = "GAMEDATA"
    SINGLE_WORD = "SINGLE_WORD"
    BLACKLIST_WORD = "BLACKLIST_WORD"
    SENSITIVE_WORD = "SENSITIVE_WORD"
    BLANK_ROW = "BLANK_ROW"
    OVERDOSE_WORD = "OVERDOSE_WORD"


def load_exists(ls: list) -> list:
    appended = []
    exists_words = util.read_list_from_folder(exists_folder)
    for word in exists_words:
        ls.append(word)
        appended.append({
            "word": word,
            "reason": WordReason.SINGLE_WORD,
            "info": "从已存在列表导入"
        })
    return appended


def filter_single_word(ls: list) -> list:
    removed = []
    for word in ls.copy():
        if len(word) == 1:
            ls.remove(word)
            removed.append({
                "word": word,
                "reason": WordReason.SINGLE_WORD,
                "conclusion": "单个字符"
            })
        pass
    return removed


def filter_blacklist_word(ls: list) -> list:
    removed = []
    blacklist_words = util.read_list_from_folder('./data/ArknightsSCELCustomData/blacklist')
    for word in ls.copy():
        if word in blacklist_words:
            ls.remove(word)
            removed.append({
                "word": word,
                "reason": WordReason.BLACKLIST_WORD,
                "conclusion": "黑名单全字匹配"
            })
    return removed


def filter_sensitive_word(ls: list) -> list:
    sensitive_keywords = util.read_list_from_folder(sensitive_folder)
    removed = []
    for word in ls.copy():
        for sensitive_keyword in sensitive_keywords:
            if sensitive_keyword in word:
                ls.remove(word)
                removed.append({
                    "word": word,
                    "reason": WordReason.SENSITIVE_WORD,
                    "conclusion": f"敏感字匹配（{sensitive_keyword}）",
                    "detail": {
                        "sensitive_keyword": sensitive_keyword
                    }
                })
                break
    return removed


def filter_blank_row(ls: list) -> list:
    removed = []
    for word in ls.copy():
        if word.replace(' ', '') == '':
            ls.remove(word)
            removed.append({
                "word": word,
                "reason": WordReason.BLANK_ROW,
                "conclusion": f"空行"
            })
    return removed


def filter_overdose_word(ls: list) -> list:
    removed = []
    for word in ls.copy():
        if len(word) >= 10:
            ls.remove(word)
            removed.append({
                "word": word,
                "reason": WordReason.OVERDOSE_WORD,
                "conclusion": f"字数大于等于10"
            })
    return removed
