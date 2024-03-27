from basicAbility import BasicAbility
from battle import enqueue_ult
import copy

class Character:
    def __init__(self, config):
        self.basic_ability = copy.deepcopy(config['basic_ability'])
        self.ult_ability = copy.deepcopy(config['ult_ability'])
        self.name = config['name']
        self.element = config['element']
        self.level = config['level']
        self.max_hp = config['hp']
        self.hp = config['hp']
        self.power = config['power']
        self.defense = config['defense']
        self.stunned = False
        self.row = config['row']
        self.column = config['column']

        self.total_dmg_dealt = 0
        self.total_dmg_taken = 0
        self.total_healing_done = 0
        self.total_healing_received = 0

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if damage < 0:  # Healing
            self.total_healing_received -= damage
        else:
            self.total_dmg_taken += damage
        if self.ult_ability is not None and damage > 0 and self.hp > 0:  # You don't get ult charge for being healed :P
            self.charge_ult(10+2*damage/self.max_hp)  # There's a minimum charge for being attacked, but big attacks will charge more
        if self.hp < 0:  # No negative HP
            self.hp = 0
        if self.hp > self.max_hp:  # Can't exceed max HP
            self.hp = self.max_hp

    def charge_ult(self, amount):
        if self.ult_ability is not None:
            self.ult_ability.charge(amount)
            if self.ult_ability.is_charged():
                print(f"{self.name}'s Ult is charged!")
                self.trigger_ult()
            enqueue_ult(self)
        else:
            # print(f"{self.name} has no Ult!")
            pass

    def use_basic_ability(self, team1, team2):
        if self.is_alive() and not self.stunned:
            self.basic_ability.use(self, team1, team2)
            self.charge_ult(20)
            return True
        return False

    def use_ult_ability(self, team1, team2):
        if self.is_alive() and not self.stunned and self.ult_ability.is_triggered() and self.ult_ability.is_charged():
            self.ult_ability.use(self, team1, team2)
            return True
        return False

    def is_ult_ready(self):
        return self.ult_ability.is_triggered() and self.ult_ability.is_charged()

    def is_ult_charged(self):
        return self.ult_ability.is_charged()

    def trigger_ult(self):
        if self.is_ult_charged():
            self.ult_ability.trigger_ult()
            return True
        return False

    def display_status(self):
        # return f"{self.name} | Level: {self.level} | HP: {self.hp}/{self.max_hp} | Power: {self.power} | Defense: {self.defense}"

        # Calculate the ratio of current health to maximum health
        health_ratio = self.hp / self.max_hp
        # Determine the number of 'filled' positions in the health bar (e.g., represented by '#')
        bar_length = 20  # Set the total length of the health bar
        health_filled_length = int(bar_length * health_ratio)
        # Create the health bar string
        health_bar = '[' + '#' * health_filled_length + '_' * (bar_length - health_filled_length) + ']'

        if self.ult_ability is not None:
            ult_filled_length = int(bar_length * self.ult_ability.get_charge_ratio())
            ult_bar = '[' + '|' * ult_filled_length + '_' * (bar_length - ult_filled_length) + ']'
        else:
            ult_bar = '[       No Ult       ]'
        # Create the status string including the health bar and numerical health
        status = f"{self.name.ljust(15)}| HP: {health_bar} {self.hp}/{str(self.max_hp)}\t | Ult: {ult_bar} | Stunned: {self.stunned}"
        return status
