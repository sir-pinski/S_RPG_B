from battle import *
from config_battles import *
from config_manager import GameConfiguration

gameconfig = GameConfiguration()
heroes = gameconfig.get_heroes()
enemies = gameconfig.get_enemies()
standard_abilities = gameconfig.get_standard_abilities()
ult_abilities = gameconfig.get_ult_abilities()
campaigns = gameconfig.get_campaigns()



# Battle(team_heroes, team_enemies)
multiple_wave_battle(team_heroes, waves)
