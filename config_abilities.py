from basicAbility import BasicAbility
from ultAbility import UltAbility
from enums import *

# Basic Abilities
slash = BasicAbility(
    name="Slash",
    mult=1.0,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.ROW,
    target_range=TargetRange.FRONT_ROW,
    target_priority=TargetPriority.CLOSEST,
    crit_rate=0.2,
    speed=10
)

poke = BasicAbility(
    name="Poke",
    mult=0.75,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.ONE,
    target_range=TargetRange.FRONT_ROW,
    target_priority=TargetPriority.CLOSEST,
    crit_rate=0.15,
    speed=15
)

sneaky_poke = BasicAbility(
    name="Sneaky Poke",
    mult=0.5,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.ONE,
    target_range=TargetRange.BACK_ROW,
    target_priority=TargetPriority.CLOSEST,
    crit_rate=0.15,
    speed=15
)

magic_missile = BasicAbility(
    name="Magic Missile",
    mult=0.6,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.THREE,
    target_range=TargetRange.ANY,
    target_priority=TargetPriority.RANDOM,
    crit_rate=0.15,
    speed=12
)

healing_touch = BasicAbility(
    name="Healing Touch",
    mult=-0.5,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ALLY_SELF,
    target_count=TargetCount.ONE,
    target_range=TargetRange.ANY,
    target_priority=TargetPriority.DAMAGED,
    crit_rate=0.2,
    speed=5
)

# Ult Abilities
firestorm = UltAbility(
    name="Firestorm",
    mult=1.2,
    effect="burn",
    effect_strength=5,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.ALL,
    target_range=TargetRange.ANY,
    target_priority=TargetPriority.NONE,
    charge_required=100,  # This represents the charge needed to use the Ult
    crit_rate=0
)

spin_attack = UltAbility(
    name="Spin Attack",
    mult=1.5,
    effect=None,
    effect_strength=None,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.ALL,
    target_range=TargetRange.FRONT_ROW,
    target_priority=TargetPriority.NONE,
    charge_required=140,  # This represents the charge needed to use the Ult
    crit_rate=0
)
