import random
import time
import queue

ult_queue = queue.Queue()


def clear_screen():
    # # For Windows
    # if os.name == 'nt':
    #     _ = os.system('cls')
    # # For macOS and Linux (name: 'posix')
    # else:
    #     _ = os.system('clear')
    print("\n" * 3)


def Battle(team1, team2):
    round_number = 1

    all_characters = team1.members + team2.members
    while team1.is_team_alive() and team2.is_team_alive():
        clear_screen()
        print("\n" * 3)
        print(f"Round {round_number}")
        if round_number == 20:
            print("**********The battle has gone on for too long!********")
        characters_to_act = [char for char in all_characters if char.is_alive() and not char.stunned]

        # Sorting characters by ability speed (descending), then randomly for ties
        characters_to_act.sort(key=lambda x: (-x.basic_ability.speed, random.random()))

        for character in characters_to_act:
            if character.is_alive() and not character.stunned:
                # for ult_trig in characters_to_act:
                #     ult_trig.trigger_ult()  # This is a little hacky, but it won't do anything unless it is ready
                while ult_queue.qsize() > 0:
                    ulting_character = ult_queue.get_nowait()
                    if ulting_character.is_ult_ready():  # Make sure Ult is still charged, and if so reset to 0 charge
                        ulting_character.use_ult_ability(team1, team2)
                character.use_basic_ability(team1, team2)
                        # for target in targets:
                        #     damage = ulting_character.activate_ult_ability(target)
                        #     print(
                        #         f"{ulting_character.name} uses ***ULT*** {ulting_character.ult_ability.name} on {target.name} for {damage} damage.")
                # Determine the target(s) based on character's ability target_type, target_count, and range
                # For this example, let's assume a simple target selection
                # targets = character.basic_ability.select_targets(character, team1, team2)
                # for target in targets:
                #     # target = random.choice(targets)  # Simple random target for example
                #     damage = character.use_basic_ability(character, target)
                #     print(f"{character.name} uses {character.basic_ability.name} on {target.name} for {damage} damage.")
                    # Check if the target has been defeated
                    # if not target.is_alive():
                    # print(f"{target.name} has been defeated!")

            # End the character's turn
            # print(f"{character.name}'s turn has ended.")

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


def check_for_charged_ults(characters):
    for character in characters:
        if character.ult_ability is not None and character.ult_ability.is_triggered():
            ult_queue.put_nowait(character)


def multiple_wave_battle(player_team, waves):
    for wave_number, enemies in enumerate(waves, start=0):
        print(f"Wave {wave_number} begins!")
        enemy_team = waves[wave_number]
        battle_result = Battle(player_team, enemy_team)  # Assuming `battle` is your battle function

        if not player_team.is_team_alive():
            print("Your team was defeated!")
            break
        elif wave_number < len(waves):
            print("Preparing for the next wave...")
            time.sleep(1)  # Optional delay before next wave
            # Consider adding some logic here for player choices or strategy changes between waves
        else:
            print("All waves defeated! Victory!")


def enqueue_ult(character):
    if character.ult_ability.is_triggered():
        ult_queue.put_nowait(character)
