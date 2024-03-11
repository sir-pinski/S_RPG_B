from character import Character
from ultAbility import UltAbility

class Boss(Character):
    def __init__(self, name, element, row, column, level, hp, power, defense, speed, basic_ability, ult_ability=None):
        super().__init__(name, element, row, column, level, hp, power, defense, speed, basic_ability)
        self.ult_ability = ult_ability
