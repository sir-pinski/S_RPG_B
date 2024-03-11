from ability import Ability

class UltAbility(Ability):
    def __init__(self, name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority, crit_rate, charge):
        super().__init__(name, mult, effect, effect_strength, target_type, target_count, target_priority, target_range, crit_rate)
        self.charge = charge
        self.current_charge = 0

    def is_charged(self):
        return self.current_charge >= self.charge

    def use(self):
        if self.is_charged():
            self.current_charge = 0
            return True
        return False
