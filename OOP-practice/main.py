from Zombie import Zombie
from Oggre import Oggre
from Hero import Hero
from Weapon import Weapon
from enemy import Enemy

def battle(enemy1: Enemy, enemy2: Enemy):
    enemy1.talk()
    enemy2.talk()

    while enemy1.health_points > 0 and enemy2.health_points > 0:
        print("________")
        enemy1.special_attack()
        enemy2.special_attack()
        print(f"{enemy1.get_type_of_enemy()}: {enemy1.health_points} HP")
        print(f"{enemy2.get_type_of_enemy()}: {enemy2.health_points} HP")
        enemy2.attack()
        enemy1.health_points -= enemy2.attack_damage
        enemy1.attack()
        enemy2.health_points -= enemy1.attack_damage

    print("________")

    if enemy1.health_points > 0:
        print(f"{enemy1.get_type_of_enemy()} wins!!!")
    else:
        print(f"{enemy2.get_type_of_enemy()} wins!!!")


def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print("________")
        enemy.special_attack()
        print(f"Hero has: {hero.health_points} HP")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP")
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print("________")

    if hero.health_points > 0:
        print("Hero wins!!!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins!!!")


zombie = Zombie(10, 1)
oggre = Oggre(20,3)
weapon = Weapon("Sword", 10)
hero = Hero(10, 1)
hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, oggre)






