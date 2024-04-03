from ability import Ability


class BasicAbility(Ability):
    def __init__(self, data):
        super().__init__(data)
        self.speed = float(data["speed"])

    # def __init__(self, name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority, crit_rate, speed):
    #     super().__init__(name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority, crit_rate)
    #     self.speed = speed
