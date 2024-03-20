from config_characters import *
from team import Team
import copy
# Teams could be formed as follows:
team_heroes = Team(members=[sleepaknight, sleepamage, sleepapaladin, sleeparogue])
battle1_wave1 = copy.deepcopy(Team(members=[firegoblin, orc, airgoblin, orc2, watergoblin]))
battle1_wave2 = copy.deepcopy(Team(members=[firegoblin, orc, airgoblin, orc2, watergoblin]))


waves = [
    battle1_wave1,  # Wave 1
    battle1_wave2  # Wave 2
    # Add more waves as needed
]
