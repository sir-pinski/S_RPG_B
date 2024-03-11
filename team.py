# This file contains the Team class, which is used to manage a team of characters in the game. The Team class is used in the battle.py file to simulate battles between teams of characters. The Team class has methods to add members to the team, check if the team is still alive, and retrieve the next living member of the team to take action in battle.
class Team:
    def __init__(self, members=None):
        self.members = members if members is not None else []
        self.team_size = len(self.members)

    def add_member(self, new_member):
        if self.team_size < 5:
            self.members.append(new_member)
            self.team_size += 1
        else:
            print("Team is already at full capacity.")

    def is_team_alive(self):
        # Check if at least one member of the team is still alive
        return any(member.is_alive() for member in self.members)

    def get_next_alive_member(self):
        # Retrieve the next living member of the team to take action in battle
        for member in self.members:
            if member.is_alive():
                return member
        return None  # If no members are alive, return None
