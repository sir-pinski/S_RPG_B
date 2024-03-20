from ability import Ability


class UltAbility(Ability):
    def __init__(self, name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority,
                 charge_required, crit_rate=0):
        super().__init__(name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority, crit_rate)
        self.charge_required = charge_required  # The amount of charge needed to use the Ult
        self.charge_current = 0  # Current charge amount
        self.triggered = False

    def use(self, caster, team1, team2):
        if self.triggered:
            self.triggered = False
            self.charge_current = 0
            print(f"U-U-U-U-U-ULTIMATE!!!")
            super().use(caster, team1, team2)
        else:
            print(f"{caster.name} tried to use {self.name} but it wasn't ready!")

    def is_charged(self):
        return self.charge_current >= self.charge_required

    def get_charge(self):
        return self.charge_current

    def get_charge_ratio(self):
        return self.charge_current / self.charge_required

    def is_triggered(self):
        return self.triggered

    def trigger_ult(self):
        if not self.is_charged():
            print(f"{self.name} is not ready!")
            return False  # Ult is not ready to be used
        # Reset charge after using the Ult
        self.triggered = True
        return True

    def charge(self, amount):
        self.charge_current += amount
        if self.charge_current > self.charge_required:  # Can't exceed required charge
            self.charge_current = self.charge_required
        if self.charge_current < 0:  # No negative charge, but charge could decrease from certain abilities
            self.charge_current = 0
