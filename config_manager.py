import requests
import csv
import io
from character import Character
import json
from ultAbility import UltAbility
from basicAbility import BasicAbility
from character_type import CharacterType

hero_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTM3NbsBnyH1FU2UEADu1PEMYYmwbHbi--mNRxudgK_cYQ6hJD-UUdPdT8HpaX-GPg0MlkzfaGFqPt-/pub?gid=2056035388&single=true&output=csv"
enemy_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTM3NbsBnyH1FU2UEADu1PEMYYmwbHbi--mNRxudgK_cYQ6hJD-UUdPdT8HpaX-GPg0MlkzfaGFqPt-/pub?gid=666264592&single=true&output=csv"
standard_ability_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTM3NbsBnyH1FU2UEADu1PEMYYmwbHbi--mNRxudgK_cYQ6hJD-UUdPdT8HpaX-GPg0MlkzfaGFqPt-/pub?gid=613308164&single=true&output=csv"
ult_ability_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTM3NbsBnyH1FU2UEADu1PEMYYmwbHbi--mNRxudgK_cYQ6hJD-UUdPdT8HpaX-GPg0MlkzfaGFqPt-/pub?gid=601283148&single=true&output=csv"
campaign_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTM3NbsBnyH1FU2UEADu1PEMYYmwbHbi--mNRxudgK_cYQ6hJD-UUdPdT8HpaX-GPg0MlkzfaGFqPt-/pub?gid=1318516599&single=true&output=csv"

force_reload = False


class GameConfiguration:
    def __init__(self):
        self.heroes = {}
        self.enemies = {}
        self.standard_abilities = {}
        self.ult_abilities = {}
        self.campaigns = {}

        load_config(self.ult_abilities, self.standard_abilities, self.enemies, self.heroes, self.campaigns)

    def get_heroes(self):
        return self.heroes

    def get_enemies(self):
        return self.enemies

    def get_standard_abilities(self):
        return self.standard_abilities

    def get_ult_abilities(self):
        return self.ult_abilities

    def get_campaigns(self):
        return self.campaigns

class BaseConfig:
    def __init__(self, config_url, type="id"):
        self.config_url = config_url
        self.local_cache_path = "cached_data/" + type + ".json"
        self.type = type
        self.data = self.load_data()

    def load_csv_from_web(self):
        response = requests.get(self.config_url)
        response.raise_for_status()
        data_dict = {}
        for row in csv.DictReader(io.StringIO(response.text)):
            unique_key = row[self.type]  # Replace 'id' with the name of your unique key
            data_dict[unique_key] = row
        return data_dict

    def save_data_to_cache(self, data):
        with open(self.local_cache_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_data_from_cache(self):
        try:
            with open(self.local_cache_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def load_data(self):
        # Attempt to load from cache first
        cached_data = self.load_data_from_cache()
        if cached_data is not None and not force_reload:
            return cached_data
        else:
            # Fetch from web and cache it for next time
            data = self.load_csv_from_web()
            self.save_data_to_cache(data)
            return data


class UltAbilitiesConfig(BaseConfig):
    def __init__(self, config_url):
        super().__init__(config_url, "id_ult_ability")  # Add any specific methods or properties for ult abilities here


class StandardAbilitiesConfig(BaseConfig):
    def __init__(self, config_url):
        super().__init__(config_url,
                         "id_std_ability")  # Add any specific methods or properties for standard abilities here


class EnemyListConfig(BaseConfig):
    def __init__(self, config_url):
        super().__init__(config_url, "id_enemy")


class HeroListConfig(BaseConfig):
    def __init__(self, config_url):
        super().__init__(config_url, "id_hero")

    # Add any specific methods or properties for heroes here
    def get_hero_by_id(self, hero_id):
        return self.data.get(hero_id, None)


class CampaignConfig(BaseConfig):
    def __init__(self, config_url):
        super().__init__(config_url, "id_campaign")  # Add any specific methods or properties for the campaign here


def load_config(ult_abilities, standard_abilities, enemies, heroes, campaign):
    ult_abilities = UltAbilitiesConfig(ult_ability_url)
    standard_abilities = StandardAbilitiesConfig(standard_ability_url)
    enemies = EnemyListConfig(enemy_url)
    heroes = HeroListConfig(hero_url)
    campaign = CampaignConfig(campaign_url)

    ult_ability_instances = {}
    for ult_ability_id, ult_ability_data in ult_abilities.data.items():
        # Assuming the UltAbility constructor takes the following parameters:
        # UltAbility(name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority, charge_required, crit_rate)
        # You'll need to adjust this to match the actual parameters of your UltAbility class
        ult_ability = UltAbility(ult_ability_data['name'], ult_ability_data['mult'], ult_ability_data['effect'],
                                 ult_ability_data['effect_strength'],
                                 ult_ability_data['target_type'], ult_ability_data['target_count'],
                                 ult_ability_data['target_range'], ult_ability_data['target_priority'],
                                 ult_ability_data['charge'], ult_ability_data['crit_rate'])
        ult_ability_instances[ult_ability_id] = ult_ability

    standard_ability_instances = {}
    for standard_ability_id, standard_ability_data in standard_abilities.data.items():
        # Assuming the BasicAbility constructor takes the following parameters:
        # BasicAbility(name, mult, effect, effect_strength, target_type, target_count, target_range, target_priority, crit_rate, speed)
        # You'll need to adjust this to match the actual parameters of your BasicAbility class
        standard_ability = BasicAbility(standard_ability_data['name'], standard_ability_data['mult'],
                                        standard_ability_data['effect'], standard_ability_data['effect_strength'],
                                        standard_ability_data['target_type'], standard_ability_data['target_count'],
                                        standard_ability_data['target_range'], standard_ability_data['target_priority'],
                                        standard_ability_data['crit_rate'], standard_ability_data['speed'])
        standard_ability_instances[standard_ability_id] = standard_ability

    hero_types = {}
    for hero_id, hero_data in heroes.data.items():
        # Assuming the Character constructor takes the following parameters:
        # CharacterType(id, name, element, base_hp, base_power, base_defense, basic_ability, ult_ability)
        # You'll need to adjust this to match the actual parameters of your Character class
        hero_type = CharacterType(hero_data['enemy_id'], hero_data['name'], hero_data['element'], hero_data['hp'], hero_data['power'],
                         hero_data['defense'], standard_abilities.data[hero_data['standard_ability']],
                         ult_abilities.data[hero_data['ult_ability']])
        hero_types[hero_id] = hero_type

    hero_instances = {}
    for hero_id, hero_data in heroes.data.items():
        # Assuming the Character constructor takes the following parameters:
        # Character(name, element, row, column, level, max_hp, attack, defense, standard_ability, ult_ability)
        # You'll need to adjust this to match the actual parameters of your Character class
        hero_types = Character(hero_data['name'], hero_data['element'], hero_data['row'], hero_data['column'],
                         hero_data['level'], hero_data['max_hp'], hero_data['attack'], hero_data['defense'],
                         standard_abilities.data[hero_data['standard_ability']],
                         ult_abilities.data[hero_data['ult_ability']])
        hero_instances[hero_id] = hero_types

    enemy_instances = {}
    for enemy_id, enemy_data in enemies.data.items():
        enemy_types = Character(enemy_data['name'], enemy_data['element'], enemy_data['row'], enemy_data['column'],
                          enemy_data['level'], enemy_data['max_hp'], enemy_data['attack'], enemy_data['defense'],
                          standard_abilities.data[enemy_data['standard_ability']],
                          ult_abilities.data[enemy_data['ult_ability']])
        enemy_instances[enemy_id] = enemy_types

    # Now you have dictionaries of Character instances for heroes and enemies, which you can use in your simulation
    # For example, to print all hero names:
    for hero_id, hero_types in hero_instances.items():
        print(hero_types.name)

    # And to print all enemy names:
    for enemy_id, enemy_types in enemy_instances.items():
        print(enemy_types.name)

    # Now you have dictionaries of BasicAbility and UltAbility instances, which you can use when creating your Character instances
    # For example, to print all ult ability names:
    for ult_ability_id, ult_ability in ult_ability_instances.items():
        print(ult_ability.name)

    # And to print all standard ability names:
    for standard_ability_id, standard_ability in standard_ability_instances.items():
        print(standard_ability.name)

# load_config(None, None, None, None, None)
