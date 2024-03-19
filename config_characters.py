from character import Character
from team import Team
from config_abilities import *

# Heroes
sleepaknight = Character("SleepaKnight", Element.FIRE, Row.FRONT, Column.LEFT, 1, 800, 40, 20, slash, None)
sleepamage = Character("SleepaMage", Element.WATER, Row.MID, Column.LEFT, 1, 500, 50, 15, magic_missile, firestorm)
sleepapaladin = Character("SleepaPaladin", Element.EARTH, Row.FRONT, Column.RIGHT, 1, 600, 45, 25, healing_touch, None)
sleeparogue = Character("SleepaRogue", Element.AIR, Row.BACK, Column.CENTER, 1, 300, 45, 10, sneaky_poke, None)


# Enemies
firegoblin = Character("Fire Goblin", Element.FIRE, Row.FRONT, Column.LEFT, 1, 200, 15, 10, poke)
airgoblin = Character("Air Goblin", Element.AIR, Row.BACK, Column.RIGHT, 1, 200, 15, 10, poke)
watergoblin = Character("Water Goblin", Element.WATER, Row.MID, Column.RIGHT, 1, 200, 15, 10, sneaky_poke)
orc = Character("Orc", Element.EARTH, Row.FRONT, Column.RIGHT, 1, 400, 25, 20, slash)
orc2 = Character("Orc2", Element.EARTH, Row.MID, Column.LEFT, 1, 400, 25, 20, slash)

