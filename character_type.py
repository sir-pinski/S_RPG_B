import copy


class CharacterType:
    def __init__(self, config):
        self.id = config['id']
        self.name = config['name']
        self.element = config['element']

        self.base_hp = config['hp']
        self.base_power = config['power']
        self.base_defense = config['defense']

        self.basic_ability = copy.deepcopy(config['basic_ability'])
        self.ult_ability = copy.deepcopy(config['ult_ability'])
