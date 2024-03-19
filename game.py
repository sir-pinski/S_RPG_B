from hero import Hero
from enemy import Enemy
from team import Team


class Game:
    def __init__(self):
        self.hero = Hero("SleepaKnight")
        self.enemies = self.generate_enemies()

    def generate_enemies(self):
        # Placeholder for enemy generation logic
        return [Enemy("Nightmare", 1, 50, 8, 5, 7)]

    def battle(self, hero, enemy):
        print(f"A wild {enemy.name} appears!")
        while hero.is_alive() and enemy.is_alive():
            hero_damage = hero.activate(enemy)
            print(f"{hero.name} deals {hero_damage} damage to {enemy.name}.")
            if enemy.is_alive():
                enemy_damage = enemy.attack - hero.defense
                if enemy_damage < 0:
                    enemy_damage = 0
                hero.take_damage(enemy_damage)
                print(f"{enemy.name} strikes back, dealing {enemy_damage} damage.")
        if hero.is_alive():
            print(f"{hero.name} has defeated {enemy.name}!")
        else:
            print("You have been defeated. Game over.")

    def start(self):
        for enemy in self.enemies:
            if self.hero.is_alive():
                self.battle(self.hero, enemy)
            else:
                break
