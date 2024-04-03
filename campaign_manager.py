from enums import Row, Column

from character import Character

class Wave_Enemy:
    def __init__(self, data):
        # Assuming data is a dictionary with keys like 'type', 'level', 'tier', and 'position'
        self.type = data.get('type')
        self.level = data.get('level', 1)  # Default level to 1 if not specified
        self.tier = data.get('tier', 1)    # Default tier to 1 if not specified
        match data.get('position'):
            case 0:
                self.row = -1
                self.column = -1
            case 1:
                self.row = Row.FRONT
                self.column = Column.LEFT
            case 2:
                self.row = Row.FRONT
                self.column = Column.CENTER
            case 3:
                self.row = Row.FRONT
                self.column = Column.RIGHT
            case 4:
                self.row = Row.MID
                self.column = Column.LEFT
            case 5:
                self.row = Row.MID
                self.column = Column.RIGHT
            case 6:
                self.row = Row.BACK
                self.column = Column.LEFT
            case 7:
                self.row = Row.BACK
                self.column = Column.CENTER
            case 8:
                self.row = Row.BACK
                self.column = Column.RIGHT




class Wave:
    def __init__(self, enemies, wave_number=0):
        self.enemies = enemies
        self.wave_number = wave_number


class Stage:
    def __init__(self, waves, stage_number=0):
        self.waves = waves
        self.stage_number = stage_number

class Act:
    def __init__(self, stages, act_number=0):
        self.stages = stages
        self.act_number = act_number


class Campaign:
    def __init__(self, acts):
        self.acts = acts


def create_enemy(enemy_data, enemy_types):
    type_id = enemy_data['type']
    # if type_id in enemy_types.data:
    #     enemy = enemy_types.data[type_id]
    #     # Adjust the dictionary with the campaign-specific data
    #     enemy_data_updated = {**enemy_data, 'level': lvl, 'tier': tier, 'position': pos}
    enemy_instance = Wave_Enemy(enemy_data)
    return enemy_instance
    # else:
    #     print(f"Character type ID '{type_id}' not found.")
    #     return None


def create_campaign(campaign_data, enemy_types):
    acts_dict = {}  # Keyed by act number, contains Act objects

    for entry_id, entry in campaign_data.items():
        # Ensure we have integers for act, stage, and wave numbers
        if entry_id == '':
            continue
        act_num = int(entry['act']) if entry['act'].isdigit() else 0
        stage_num = int(entry['stage']) if entry['stage'].isdigit() else 0
        wave_id = entry['id']  # Using id as a unique identifier for each wave

        # Construct enemy list for this wave
        enemies = [
            create_enemy({
                'type': entry[f'enemy_{i}_type'],
                'level': int(entry.get(f'enemy_{i}_lvl', '0')),
                'tier': int(entry.get(f'enemy_{i}_tier', '0')),
                'position': int(entry.get(f'enemy_{i}_pos', '0'))
            }, enemy_types)
            for i in range(1, 6) if entry.get(f'enemy_{i}_type')
        ]

        # Construct the wave
        wave = Wave(enemies, wave_number=wave_id)

        # Append the wave to the correct act and stage
        if act_num not in acts_dict:
            acts_dict[act_num] = Act([], act_number=act_num)

        # Find or create the stage within the act
        act = acts_dict[act_num]
        stage = next((s for s in act.stages if s.stage_number == stage_num), None)
        if not stage:
            stage = Stage([], stage_number=stage_num)
            act.stages.append(stage)

        # Append the wave to the stage
        stage.waves.append(wave)

    # Now we have a dictionary of acts, each containing a list of stages, which in turn contain lists of waves
    sorted_acts = [act for _, act in sorted(acts_dict.items(), key=lambda x: x[0])]

    return Campaign(sorted_acts)