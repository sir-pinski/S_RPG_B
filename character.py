from basicAbility import BasicAbility

class Character:
    def __init__(self, name, element, level=1, hp=100, power=10, defense=10, basic_ability=None):
        self.basic_ability = basic_ability
        self.name = name
        self.element = element
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.defense = defense
        self.stunned = False

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:  # No negative HP
            self.hp = 0
        if self.hp > self.max_hp:  # Can't exceed max HP
            self.hp = self.max_hp

    def display_status(self):
        # return f"{self.name} | Level: {self.level} | HP: {self.hp}/{self.max_hp} | Power: {self.power} | Defense: {self.defense}"

        # Calculate the ratio of current health to maximum health
        health_ratio = self.hp / self.max_hp
        # Determine the number of 'filled' positions in the health bar (e.g., represented by '#')
        bar_length = 20  # Set the total length of the health bar
        filled_length = int(bar_length * health_ratio)
        # Create the health bar string
        health_bar = '[' + '#' * filled_length + '_' * (bar_length - filled_length) + ']'
        # Create the status string including the health bar and numerical health
        status = f"{self.name} | HP: {health_bar} {self.hp}/{self.max_hp}"
        return status
