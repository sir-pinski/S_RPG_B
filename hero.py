from character import Character
from ultAbility import UltAbility

class Hero(Character):
    def __init__(self, name, element, level, hp, power, defense, basic_ability, ult_ability=None):
        super().__init__(name, element, level, hp, power, defense, basic_ability)
        self.ult_ability = ult_ability
        # self.equipment = equipment if equipment else {}

    def use_ultimate(self, target):
        if self.ultimate and self.hp > 0:  # Check if ultimate ability exists and hero is alive
            return self.ultimate.cast(target)
        return 0  # If no ultimate ability or hero is not alive, return 0 damage