from ability import Ability


class UltAbility(Ability):
    def __init__(self, name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority,
                 charge_required, crit_rate=0):
        super().__init__(name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority, crit_rate)
        self.charge_required = charge_required  # The amount of charge needed to use the Ult
        self.charge_current = 0  # Current charge amount

    def is_charged(self):
        return self.charge_current >= self.charge_required

    def trigger_ult(self):
        if not self.is_charged():
            return False  # Ult is not ready to be used
        # Reset charge after using the Ult
        self.charge_current = 0
        return True

    def charge(self, amount):
        self.charge_current += amount
        if self.charge_current > self.charge_required:
            self.charge_current = self.charge_required
