from battle import *
from campaign_manager import create_campaign
from character import Character
from config_manager import GameConfiguration
from enums import Element, Column, Row

gameconfig = GameConfiguration()
heroes = gameconfig.get_heroes()
enemies = gameconfig.get_enemies()
standard_abilities = gameconfig.get_standard_abilities()
ult_abilities = gameconfig.get_ult_abilities()
campaign = gameconfig.get_campaign()
multipliers = gameconfig.get_multipliers()

# Heroes

# hero_instances = []
# Assuming `heroes` is an instance of HeroListConfig
# for hero_id, hero_data in heroes.data.items():
#     hero_instances.append(Character(hero_data, hero_data['level'], hero_data['tier'], hero_data['row'], hero_data['column']))

hero_team = Team(
    [
        Character(standard_abilities, ult_abilities, multipliers, heroes.data["hero1"], 1, 1, Row.FRONT, Column.LEFT),
        Character(standard_abilities, ult_abilities, multipliers, heroes.data["hero2"], 1, 1, Row.MID, Column.LEFT),
        Character(standard_abilities, ult_abilities, multipliers, heroes.data["hero3"], 1, 1, Row.FRONT, Column.RIGHT)
        # Character("hero4", 1, 1, Row.BACK, Column.CENTER)

    ]
)

# sleepaknight = Character("SleepaKnight", Element.FIRE, Row.FRONT, Column.LEFT, 1, 800, 40, 20, slash, spin_attack)
# sleepamage = Character("SleepaMage", Element.WATER, Row.MID, Column.LEFT, 1, 500, 50, 15, magic_missile, firestorm)
# sleepapaladin = Character("SleepaPaladin", Element.EARTH, Row.FRONT, Column.RIGHT, 1, 600, 45, 25, healing_touch, None)
# sleeparogue = Character("SleepaRogue", Element.AIR, Row.BACK, Column.CENTER, 1, 300, 45, 10, sneaky_poke, None)


# Assuming 'campaigns' is your input data dictionary
campaign_object = create_campaign(gameconfig)
# battle = Battle(campaign_object, heroes, 1, 1)
print("1")
Battle(campaign_object, gameconfig, hero_team, 1, 8).simulate_battle()
# multiple_wave_battle(campaign_object)
