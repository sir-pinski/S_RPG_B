import random
import os
import time


def clear_screen():
    # # For Windows
    # if os.name == 'nt':
    #     _ = os.system('cls')
    # # For macOS and Linux (name: 'posix')
    # else:
    #     _ = os.system('clear')
    print("\n"*10)


def Battle(team1, team2):
    round_number = 1
    all_characters = team1.members + team2.members
    while team1.is_team_alive() and team2.is_team_alive():
        clear_screen()
        print("\n" * 3)
        print(f"Round {round_number}")
        if round_number > 1:
            characters_to_act = [char for char in all_characters if char.is_alive() and not char.stunned]
        else:  # First round, only team1 acts
            characters_to_act = [char for char in team1.members if char.is_alive()]

        # Sorting characters by ability speed (descending), then randomly for ties
        characters_to_act.sort(key=lambda x: (-x.basic_ability.speed, random.random()))

        for character in characters_to_act:
            if character.is_alive() and not character.stunned:
                # Determine the target(s) based on character's ability target_type, target_count, and range
                # For this example, let's assume a simple target selection
                targets = character.basic_ability.find_targets(character, team1, team2)
                for target in targets:
                    # target = random.choice(targets)  # Simple random target for example
                    damage = character.basic_ability.deal_damage(character, target)
                    print(f"{character.name} uses {character.basic_ability.name} on {target.name} for {damage} damage.")
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
        time.sleep(0.1)

    # Determine and announce the winner
    if team1.is_team_alive():
        print("Team 1 is victorious!")
    else:
        print("Team 2 is victorious!")
