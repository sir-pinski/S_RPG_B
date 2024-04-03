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
        self.campaign = {}

        load_config(self)
        # load_config(self.ult_abilities, self.standard_abilities, self.enemies, self.heroes, self.campaigns)

    def get_heroes(self):
        return self.heroes

    def get_enemies(self):
        return self.enemies

    def get_standard_abilities(self):
        return self.standard_abilities

    def get_ult_abilities(self):
        return self.ult_abilities

    def get_campaign(self):
        return self.campaign

class BaseConfig:
    def __init__(self, config_url, type="id"):
        self.config_url = config_url
        self.local_cache_path = "cached_data/" + type + ".json"
        self.type = type
        self.data = self.load_data()
        print("loaded")

    def load_csv_from_web(self):
        response = requests.get(self.config_url)
        response.raise_for_status()

        # Convert the CSV text to a list of rows, each being a list of cell values
        rows = list(csv.reader(io.StringIO(response.text)))

        # Extract the first two rows for column inclusion flags and headers
        inclusion_flags = rows[0]
        headers = rows[1]

        # Filter out columns based on inclusion flags set to "True"
        columns_to_include = [header for flag, header in zip(inclusion_flags, headers) if flag.lower() == 'true']

        data_dict = {}
        for row in rows[2:]:  # Skip the first two rows and iterate through the rest
            row_dict = {header: value for header, value in zip(headers, row) if header in columns_to_include}
            # if self.type in row_dict:  # Ensure the unique key column is included and has a value
            unique_key = row_dict['id']
            data_dict[unique_key] = row_dict

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

    # # Add any specific methods or properties for heroes here
    # def get_hero_by_id(self, hero_id):
    #     return self.data.get(hero_id, None)


class CampaignConfig(BaseConfig):
    def __init__(self, config_url):
        super().__init__(config_url, "id_campaign")  # Add any specific methods or properties for the campaign here


def load_config(self):
    self.ult_abilities = UltAbilitiesConfig(ult_ability_url)
    self.standard_abilities = StandardAbilitiesConfig(standard_ability_url)
    self.enemies = EnemyListConfig(enemy_url)
    self.heroes = HeroListConfig(hero_url)
    self.campaign = CampaignConfig(campaign_url)

    ult_ability_types = {}
    for ult_ability_id, ult_ability_data in self.ult_abilities.data.items():
        ult_ability = UltAbility(ult_ability_data)
        ult_ability_types[ult_ability_id] = ult_ability

    standard_ability_types = {}
    for standard_ability_id, standard_ability_data in self.standard_abilities.data.items():
        standard_ability = BasicAbility(standard_ability_data)
        standard_ability_types[standard_ability_id] = standard_ability

    hero_types = {}
    for hero_id, hero_data in self.heroes.data.items():
        hero_type = CharacterType(hero_data)
        hero_types[hero_id] = hero_type

    enemy_types = {}
    for enemy_id, enemy_data in self.enemies.data.items():
        enemy_type = CharacterType(enemy_data)
        enemy_types[enemy_id] = enemy_type

    campaign = {}
    for campaign_id, campaign_data in self.campaign.data.items():
        campaign[campaign_id] = campaign_data

    # Now you have dictionaries of CharacterType instances for heroes and enemies, which you can use in your simulation
    # For example, to print all hero names:
    for hero_id, hero_type in hero_types.items():
        print(hero_type.name)

    # And to print all enemy names:
    for enemy_id, enemy_type in enemy_types.items():
        print(enemy_type.name)

    # Now you have dictionaries of BasicAbility and UltAbility instances, which you can use when creating your Character instances
    # For example, to print all ult ability names:
    for ult_ability_id, ult_ability in ult_ability_types.items():
        print(ult_ability.name)

    # And to print all standard ability names:
    for standard_ability_id, standard_ability in standard_ability_types.items():
        print(standard_ability.name)

# load_config(None, None, None, None, None)
