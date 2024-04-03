import math
import random
from enums import *


class Ability:
    debug = False

    # def __init__(self, name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority,
    #              crit_rate=0):
    #     self.name = name
    #     self.mult = mult  # Multiplier for the ability. Negative for heals.
    #     self.effect = effect
    #     self.effect_strength = effect_strength
    #     self.target_type = target_type
    #     self.target_count = target_count
    #     self.target_range = target_range
    #     self.target_priority = target_priority  # Placeholder for future implementation
    #     self.crit_rate = crit_rate

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.mult = float(data['mult'])  # Multiplier for the ability. Negative for heals.
        self.effect = data['effect']
        self.effect_strength = float(data['effect_strength'])
        # Convert string values to enum members
        self.target_type = TargetType[data['target_type']]
        self.target_count = TargetCount[data['target_count']]
        self.target_range = TargetRange[data['target_range']]
        self.target_priority = TargetPriority[data['target_priority']]  # Placeholder for future implementation
        self.crit_rate = float(data['crit_rate'])

    def use(self, caster, team1, team2):
        total_damage = 0
        targets = self.select_targets(caster, team1, team2)
        for target in targets:
            damage = self.activate(caster, target)
            if damage < 0:
                caster.total_healing_done -= damage
            else:
                caster.total_dmg_dealt += damage
            print(f"{caster.name} uses {self.name} on {target.name} for {damage} damage.")

    def select_targets(self, caster, team1, team2):
        possible_targets = self.identify_targets(caster, team1, team2)
        prioritized_targets = self.prioritize_targets(caster, possible_targets)
        final_targets = []
        for character in prioritized_targets:
            match self.target_count:
                case TargetCount.ONE:
                    if character.is_alive() and len(final_targets) < 1:
                        final_targets.append(character)
                case TargetCount.TWO:
                    if character.is_alive() and len(final_targets) < 2:
                        final_targets.append(character)
                case TargetCount.THREE:
                    if character.is_alive() and len(final_targets) < 3:
                        final_targets.append(character)
                case TargetCount.FOUR:
                    if character.is_alive() and len(final_targets) < 4:
                        final_targets.append(character)
                case TargetCount.ALL:
                    if character.is_alive():
                        final_targets.append(character)
                case TargetCount.COLUMN:
                    pass  # Placeholder for future implementation
                case TargetCount.ROW:
                    if character.is_alive() and len(final_targets) < 1:
                        final_targets.append(character)
                    elif character.is_alive() and len(final_targets) < 2 and character.row == final_targets[0].row:
                        final_targets.append(character)
                case TargetCount.SPLASH:
                    pass  # Placeholder for future implementation
        return final_targets

    def identify_targets(self, caster, team1, team2):
        targets = []

        # Identify allies and enemies
        if caster in team1.members:
            allies = team1.copy()
            enemies = team2.copy()
        else:
            allies = team2.copy()
            enemies = team1.copy()

        match self.target_type:
            case TargetType.ALLY:
                for character in allies.members:
                    if character.is_alive():
                        if character != caster:
                            targets.append(character)

            case TargetType.ALLY_SELF:
                for character in allies.members:
                    if character.is_alive():
                        targets.append(character)

            case TargetType.SELF:
                targets.append(caster)

            case TargetType.EVERYONE:
                for character in allies.members + enemies.members:
                    if character.is_alive():
                        targets.append(character)

            # Targeting Ranges only apply for Enemy targeting types. In all other types it is assumed to be "Any"
            case TargetType.ENEMY:
                for character in enemies.members:
                    if character.is_alive():
                        match self.target_range:
                            case TargetRange.ANY:
                                targets.append(character)
                            case TargetRange.FRONT_ROW:
                                if character.row == enemies.identify_front():
                                    targets.append(character)
                            case TargetRange.BACK_ROW:
                                if character.row == enemies.identify_back():
                                    targets.append(character)
        return targets

    def prioritize_targets(self, caster, targets):
        prioritized_targets = []
        match self.target_priority:
            case TargetPriority.NONE:
                prioritized_targets = targets
            case TargetPriority.RANDOM:
                random.shuffle(targets)
                prioritized_targets = targets
            case TargetPriority.CLOSEST:
                targets.sort(key=lambda x: (x.row, Column.distance(caster.column, x.column)))
                prioritized_targets = targets
            case TargetPriority.DAMAGED:
                targets.sort(key=lambda x: (x.hp / x.max_hp, random.random()))
                prioritized_targets = targets
        return prioritized_targets

    def activate(self, caster, target):
        # Implement the logic for casting the ability
        # This is a placeholder for the actual implementation
        if self.debug:
            print(f"---{caster.name} uses {self.name} on {target.name}.---")
        damage = caster.power * self.mult  # initial raw damage
        if self.debug:
            print(f"Base damage: {damage}")
        damage = damage * (
            2 if random.random() < self.crit_rate else 1)  # determine if crit hit (we do this prior to defense)
        if self.debug:
            print(f"Damage after crit: {damage}")
        if self.mult < 0:  # if this is a heal, return here and ignore element and defense
            damage = math.ceil(damage)
            if self.debug:
                print(f"Healing: {damage}")
            target.take_damage(damage)
            return damage
        damage = damage * element_multiplier(caster, target)  # apply element multiplier
        if self.debug:
            print(f"Element multiplier: {element_multiplier(caster, target)}, Damage after element: {damage}")
        damage = damage * (damage / (damage + target.defense))  # apply defense
        damage = math.ceil(damage)  # take floor to avoid annoying float numbers, but guarantee at least 1 damage
        if self.debug:
            print(f"Defense: {target.defense}, Damage after defense: {damage}")
        target.take_damage(damage)
        return damage
