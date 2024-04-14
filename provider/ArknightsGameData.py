import util
import os

from ._base import Provider


class ArknightsGameData(Provider):
    def __init__(self, config: dict) -> None:
        super().__init__(config)
        self.types = config.get('types', ['act', 'char', 'charm', 'crisis', 'enemy', 'gacha', 'term', 'item', 'rogue', 'skill', 'skin', 'stage', 'sub_prof'])
        self.basic_path = os.path.join(self.config.get('path'), 'zh_CN', 'gamedata')

    def get(self) -> list[str]:
        ls = []

        def append(value):
            ls.append(value)

        if 'act' in self.types:
            activity_table = util.read_json(f"{self.basic_path}/excel/activity_table.json")
            # 活动名字
            for bsi in activity_table['basicInfo']:
                word = activity_table['basicInfo'][bsi]['name']

                if all(keyword not in word for keyword in ["活动", "签到", "复刻", "任务", "登录领取奖励"]):
                    for word in util.split_text_by_symbols(word):
                        append(word)

        if 'char' in self.types:
            character_table = util.read_json(f"{self.basic_path}/excel/character_table.json")
            # 干员名
            for per in character_table:
                word = character_table[per]['name']
                append(word)

        if 'charm' in self.types:
            charm_table = util.read_json(f"{self.basic_path}/excel/charm_table.json")
            # charm(多索雷斯那一堆标签)
            for charm in charm_table['charmList']:
                word = charm['name']
                for word in util.split_text_by_symbols(word):
                    append(word)

        if 'crisis' in self.types:
            crisis_table = util.read_json(f"{self.basic_path}/excel/crisis_table.json")
            # 危机合约名称
            for crisis in crisis_table['seasonInfo']:
                word = crisis['name']
                append(word)

        if 'enemy' in self.types:
            enemy_handbook_table = util.read_json(f"{self.basic_path}/excel/enemy_handbook_table.json")
            # 敌人名称
            for enemy in enemy_handbook_table['enemyData']:
                word = enemy_handbook_table['enemyData'][enemy]['name']
                append(word)

        if 'gacha' in self.types:
            gacha_table = util.read_json(f"{self.basic_path}/excel/gacha_table.json")
            # 卡池名称
            for gacha in gacha_table['gachaPoolClient']:
                word = gacha['gachaPoolName']
                if all(keyword not in word for keyword in ["适合多种场合的强力干员"]):
                    for word in util.split_text_by_symbols(word):
                        append(word)

        if 'term' in self.types:
            gamedata_const = util.read_json(f"{self.basic_path}/excel/gamedata_const.json")
            # 术语名称
            for term in gamedata_const['termDescriptionDict']:
                word = gamedata_const['termDescriptionDict'][term]['termName']
                for word in util.split_text_by_symbols(word):
                    append(word)

        if 'item' in self.types:
            item_table = util.read_json(f"{self.basic_path}/excel/item_table.json")
            # 物品名称
            for item in item_table['items']:
                word = item_table['items'][item]['name']
                if all(keyword not in word for keyword in ["信物", "寻访凭证", "家具"]):
                    append(word)

        if 'rogue' in self.types:
            roguelike_topic_table = util.read_json(f"{self.basic_path}/excel/roguelike_topic_table.json")
            # 肉鸽
            for item in roguelike_topic_table['details']:
                for rogue_type in roguelike_topic_table['details']:
                    rogue_detail = roguelike_topic_table['details'][rogue_type]

                    for challenge in rogue_detail['challenges']:
                        word = rogue_detail['challenges'][challenge]['challengeName']
                        append(word)
                    for stage in rogue_detail['stages']:
                        word = rogue_detail['stages'][stage]['name']
                        append(word)
                    for nodeTypeData in rogue_detail['nodeTypeData']:
                        word = rogue_detail['nodeTypeData'][nodeTypeData]['name']
                        append(word)
                    for items in rogue_detail['items']:
                        word = rogue_detail['items'][items]['name']
                        if all(keyword not in word for keyword in ["招募券", "给"]):
                            for word in util.split_text_by_symbols(word):
                                append(word)

        if 'skill' in self.types:
            skill_table = util.read_json(f"{self.basic_path}/excel/skill_table.json")
            # 技能名
            for skill in skill_table:
                for skill_level in skill_table[skill]['levels']:
                    word = skill_level['name'].split('·')[0]
                    for word in util.split_text_by_symbols(word):
                        append(word)

        if 'skin' in self.types:
            skin_table = util.read_json(f"{self.basic_path}/excel/skin_table.json")
            # 皮肤名
            for skin in skin_table['charSkins']:
                word = skin_table['charSkins'][skin]['displaySkin']['skinName']
                for word in util.split_text_by_symbols(word):
                    append(word)

        if 'stage' in self.types:
            stage_table = util.read_json(f"{self.basic_path}/excel/stage_table.json")
            # 关卡名
            for stage in stage_table['stages']:
                word = stage_table['stages'][stage]['name']
                append(word)

        if 'sub_prof' in self.types:
            uniequip_data = util.read_json(f"{self.basic_path}/excel/uniequip_data.json")
            # 分支名
            for subProf in uniequip_data['subProfDict']:
                word = uniequip_data['subProfDict'][subProf]['subProfessionName']
                if all(keyword not in word for keyword in ["干员附带单位", "无职业陷阱", "预留"]):
                    append(word)

        return ls
