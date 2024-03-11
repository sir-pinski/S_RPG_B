import math
import random
from enums import *


class Ability:
    def __init__(self, name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority,
                 crit_rate=0):
        self.name = name
        self.mult = mult  # Multiplier for the ability. Negative for heals.
        self.effect = effect
        self.effect_strength = effect_strength
        self.target_type = target_type
        self.target_count = target_count
        self.target_range = target_range
        self.target_priority = target_priority  # Placeholder for future implementation
        self.crit_rate = crit_rate

    def find_targets(self, caster, team1, team2):
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
        return final_targets

    def identify_targets(self, caster, team1, team2):
        targets = []
        if caster in team1.members:
            allies = team1.members.copy()
            enemies = team2.members.copy()
        else:
            allies = team2.members.copy()
            enemies = team1.members.copy()

        if self.target_type == TargetType.ALLY:
            for character in allies:
                if character != caster:
                    targets.append(character)

        elif self.target_type == TargetType.ALLY_SELF:
            for character in allies:
                targets.append(character)

        elif self.target_type == TargetType.SELF:
            targets.append(caster)

        elif self.target_type == TargetType.EVERYONE:
            for character in allies + enemies:
                targets.append(character)

        elif self.target_type == TargetType.ENEMY:
            for character in enemies:
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
                # Need to add logic to prioritize closest targets
                prioritized_targets = targets
            case TargetPriority.DAMAGED:
                targets.sort(key=lambda x: (x.hp / x.max_hp, random.random()))
                prioritized_targets = targets
        return prioritized_targets

    def deal_damage(self, caster, target):
        # Implement the logic for casting the ability
        # This is a placeholder for the actual implementation
        damage = caster.power * self.mult  # initial raw damage
        damage = damage * (2 if random.random() < self.crit_rate else 1)  # determine if crit hit (we do this prior to defense)
        if self.mult < 0:  # if this is a heal, return here and ignore element and defense
            damage = math.ceil(damage)
            target.take_damage(damage)
            return damage
        damage = damage * element_multiplier(caster, target)  # apply element multiplier
        damage = damage * (damage / (damage + target.defense))  # apply defense
        damage = math.ceil(damage)  # take floor to avoid annoying float numbers, but guarantee at least 1 damage
        target.take_damage(damage)
        return damage
