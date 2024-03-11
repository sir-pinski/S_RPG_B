from hero import Hero
from character import Character
from team import Team
from config_abilities import *

# Heroes
sleepaknight = Hero("SleepaKnight", Element.FIRE, Row.FRONT, Column.LEFT, 1, 1000, 10, 12, slash, None)
sleepamage = Hero("SleepaMage", Element.WATER, Row.MID, Column.LEFT, 1, 800, 13, 8, magic_missile, firestorm)
sleepapriest = Hero("SleepaPriest", Element.EARTH, Row.MID, Column.RIGHT, 1, 500, 11, 5, healing_touch, None)

# Enemies
firegoblin = Character("Fire Goblin", Element.FIRE, Row.FRONT, Column.LEFT, 1, 500, 5, 6, poke)
airgoblin = Character("Air Goblin", Element.AIR, Row.BACK, Column.CENTER, 1, 500, 5, 6, poke)
watergoblin = Character("Water Goblin", Element.WATER, Row.MID, Column.RIGHT, 1, 500, 5, 6, poke)
orc = Character("Orc", Element.EARTH, Row.FRONT, Column.RIGHT, 1, 800, 15, 12, slash)
orc2 = Character("Orc", Element.EARTH, Row.MID, Column.LEFT, 1, 800, 15, 12, slash)

# Teams could be formed as follows:
team_heroes = Team(members=[sleepaknight, sleepamage, sleepapriest])
team_enemies = Team(members=[firegoblin, orc, airgoblin, orc2, watergoblin])