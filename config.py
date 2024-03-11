from hero import Hero
from character import Character
from team import Team
from basicAbility import BasicAbility
from ultAbility import UltAbility
from enums import *
from battle import Battle


# Basic Abilities
slash = BasicAbility(
    name="Slash",
    mult=1.0,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.TWO,
    target_range=TargetRange.FRONT_ROW,
    target_priority=TargetPriority.CLOSEST,
    crit_rate=0.2,
    speed=10
)

poke = BasicAbility(
    name="Poke",
    mult=0.5,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.ONE,
    target_range=TargetRange.FRONT_ROW,
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
    mult=-0.7,
    effect="none",
    effect_strength=0,
    target_type=TargetType.ALLY_SELF,
    target_count=TargetCount.TWO,
    target_range=TargetRange.ANY,
    target_priority=TargetPriority.DAMAGED,
    crit_rate=0.2,
    speed=5
)

# Ult Abilities
firestorm = UltAbility(
    name="Firestorm",
    mult=2.0,
    effect="burn",
    effect_strength=5,
    target_type=TargetType.ENEMY,
    target_count=TargetCount.ALL,
    target_range=TargetRange.ANY,
    target_priority=TargetPriority.NONE,
    crit_rate=0,
    charge=100  # This represents the charge needed to use the Ult
)

# Heroes
sleepaknight = Hero("SleepaKnight", Element.FIRE, 1, 1000, 10, 12, slash, None)
sleepamage = Hero("SleepaMage", Element.WATER, 1, 800, 13, 8, magic_missile, firestorm)
sleepapriest = Hero("SleepaPriest", Element.EARTH, 1, 500, 11, 5, healing_touch, None)

# Enemies
firegoblin = Character("Fire Goblin", Element.FIRE, 1, 500, 5, 6, poke)
airgoblin = Character("Air Goblin", Element.AIR, 1, 500, 5, 6, poke)
watergoblin = Character("Water Goblin", Element.WATER, 1, 500, 5, 6, poke)
orc = Character("Orc", Element.EARTH, 1, 800, 15, 12, slash)
orc2 = Character("Orc", Element.EARTH, 1, 800, 15, 12, slash)

# Teams could be formed as follows:
team_heroes = Team(members=[sleepaknight, sleepamage, sleepapriest])
team_enemies = Team(members=[firegoblin, orc, airgoblin, orc2, watergoblin])