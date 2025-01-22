from enemy import Enemy
import random

class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print("Orrrrrrr")

    def spread_disease(self):
        print("Zombie is trying to spread infection.")

    def special_attack(self):
        did_special_attack = random.random() < 0.50
        if did_special_attack:
            self.health_points += 2
            print("Zombie regenerated")
