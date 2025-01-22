class Enemy:

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy: str = type_of_enemy
        self.health_points: int = health_points
        self.attack_damage: int = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I'm an enemy! Prepare to fight")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} walks closer to you!")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks with damage {self.attack_damage}")

    def special_attack(self):
        print("Enemy has no special attack.")