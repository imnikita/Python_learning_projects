import random

from enemy import Enemy

class Oggre(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Oggre",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print(f"{self.get_type_of_enemy()} slams his hands!")

    def special_attack(self):
        did_special_attack = random.random() < 0.20
        if did_special_attack:
            self.attack_damage += 4
            print("Oggre gets angry and increases attack by 4.")