import random
import time
import queue

from character import Character
from team import Team



#
def clear_screen():
    # # For Windows
    # if os.name == 'nt':
    #     _ = os.system('cls')
    # # For macOS and Linux (name: 'posix')
    # else:
    #     _ = os.system('clear')
    print("\n" * 3)


#
#
# def battle(team1, team2):
#     round_number = 1
#
#     all_characters = team1.members + team2.members
#     while team1.is_team_alive() and team2.is_team_alive():
#         clear_screen()
#         print("\n" * 3)
#         print(f"Round {round_number}")
#         # if round_number == 20:
#         #     print("********The battle has gone on for too long!********")
#         characters_to_act = [char for char in all_characters if char.is_alive() and not char.stunned]
#
#         # Sorting characters by ability speed (descending), then randomly for ties
#         characters_to_act.sort(key=lambda x: (-x.basic_ability.speed, random.random()))
#
#         for character in characters_to_act:
#             if character.is_alive() and not character.stunned:
#                 while ult_queue.qsize() > 0:
#                     ulting_character = ult_queue.get_nowait()
#                     if ulting_character.is_ult_ready():  # Make sure Ult is still charged, and if so reset to 0 charge
#                         ulting_character.use_ult_ability(team1, team2)
#                 character.use_basic_ability(team1, team2)
#
#         # Check for end of round conditions, reset characters for next round, etc.
#         round_number += 1
#
#         print("\n")
#         for character in team1.members:
#             print(character.display_status())
#             character.stunned = False  # Example of resetting status
#         print("\n")
#         for character in team2.members:
#             print(character.display_status())
#             character.stunned = False  # Example of resetting status
#         time.sleep(0.2)
#
#     # Determine and announce the winner
#     if team1.is_team_alive():
#         print("Team 1 is victorious!")
#         return True
#     else:
#         print("Team 2 is victorious!")
#         return False
#
#
# def check_for_charged_ults(characters):
#     for character in characters:
#         if character.ult_ability is not None and character.ult_ability.is_triggered():
#             ult_queue.put_nowait(character)
#
#
# def multiple_wave_battle(campaign_data):
#     for wave_number, enemies in enumerate(waves, start=0):
#         print(f"Wave {wave_number} begins!")
#         enemy_team = waves[wave_number]
#         battle_result = battle(player_team, enemy_team)  # Assuming `battle` is your battle function
#
#         if not player_team.is_team_alive():
#             print("Your team was defeated!")
#             break
#         elif wave_number < len(waves) - 1:
#             print("Preparing for the next wave...")
#             time.sleep(1)  # Optional delay before next wave
#             # Consider adding some logic here for player choices or strategy changes between waves
#         else:
#             print("All waves defeated! Victory!")
#
#
# def enqueue_ult(character):
#     if character.ult_ability.is_triggered():
#         ult_queue.put_nowait(character)


class Battle:
    def __init__(self, campaign, player_team, enemy_types, standard_abilities, ult_abilities, start_wave_id=None, end_wave_id=None):
        self.campaign = campaign
        self.player_team = player_team
        self.enemy_types = enemy_types
        self.standard_abilities = standard_abilities
        self.ult_abilities = ult_abilities
        self.start_wave_id = start_wave_id
        self.end_wave_id = end_wave_id
        self.ult_queue = queue.Queue()

    def simulate_battle(self):
        for act in self.campaign.acts:
            for stage in act.stages:
                for wave in stage.waves:
                    wave_id = int(wave.wave_number)
                    if self.start_wave_id and wave_id < self.start_wave_id:
                        continue
                    if self.end_wave_id and wave_id > self.end_wave_id:
                        break

                    enemy_team_members = [
                        Character(
                            self.standard_abilities,
                            self.ult_abilities,
                            self.enemy_types.data[enemy.type],
                            # Adjust this dictionary structure to match what Character expects
                            enemy.level,
                            enemy.tier,
                            enemy.row,
                            enemy.column,
                            # Include other necessary attributes here
                        )
                        for enemy in wave.enemies
                    ]

                    enemy_team = Team(enemy_team_members)

                    print(f"\nStarting battle for Wave ID: {wave_id}")
                    self.battle(self.player_team, enemy_team)

                    if not self.player_team.is_team_alive():
                        print("Player team defeated!")
                        return False

        print("All waves completed or specified range of waves defeated.")
        return True

    def battle(self, team1, team2):
        round_number = 1

        all_characters = team1.members + team2.members
        while team1.is_team_alive() and team2.is_team_alive():
            clear_screen()
            print("\n" * 3)
            print(f"Round {round_number}")
            # if round_number == 20:
            #     print("********The battle has gone on for too long!********")
            characters_to_act = [char for char in all_characters if char.is_alive() and not char.stunned]

            # Sorting characters by ability speed (descending), then randomly for ties
            characters_to_act.sort(key=lambda x: (-x.basic_ability.speed, random.random()))

            for character in characters_to_act:
                if character.is_alive() and not character.stunned:
                    self.manage_ult_queue(team1, team2)
                    while self.ult_queue.qsize() > 0:
                        ulting_character = self.ult_queue.get_nowait()
                        if ulting_character.is_ult_ready():  # Make sure Ult is still charged, and if so reset to 0 charge
                            ulting_character.use_ult_ability(team1, team2)
                    character.use_basic_ability(team1, team2)

            # Check for end of round conditions, reset characters for next round, etc.
            round_number += 1

            print("\n")
            for character in team1.members:
                print(character.display_status())
                character.stunned = False  # Example of resetting status
            print("\n")
            for character in team2.members:
                print(character.display_status())
                character.stunned = False  # Example of resetting status
            time.sleep(0.2)

            # Determine and announce the winner
        if team1.is_team_alive():
            print("Team 1 is victorious!")
            return True
        else:
            print("Team 2 is victorious!")
            return False

    # @staticmethod
    # def enqueue_ult(character, ult_queue):
    #     """Enqueue characters with charged ults."""
    #     if character.is_ult_ready():
    #         ult_queue.put_nowait(character)
    # Example: Function to manage ult queue based on characters' ult charge status
    def manage_ult_queue(self, team1, team2):
        for character in team1.members + team2.members:
            if character.is_ult_ready():
                self.ult_queue.put_nowait(character)
