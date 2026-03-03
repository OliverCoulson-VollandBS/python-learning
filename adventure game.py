import random

class Player():

    def __init__(self, name, health, attack_damage, gold, sword):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.gold = gold
        self.sword = sword

    def info(self):
        print((f"You are called {self.name}, have {self.health} health, have {self.mana} mana, have {self.attack_damage} attack damage, have {self.armour} armour, have {self.gold} gold and a {self.sword} for a weapon."))


class Enemy():

    def __init__(self, name, health, attack_damage, gold_given):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.gold_given = gold_given

    def enemy_fight(self):
        enemy_fighting = enemy_spawn()
        while 


        def enemy_spawn(self):
        monster_names = ["Goblin", "Fluffy Monster", "Evil Stron monster"]
        self.health = random.randint(10,50)
        self.attack_damage = random.randint(5,25)
        if self.attack_damage < 12:
            self.name = monster_names[0]
        elif self.attack_damage >= 12 and self.attack_damage < 20:
            self.name = monster_names[1]
        else:
            self.name = monster_names[2]
        print(f"{self.name} is here! it does {self.attack_damage} damage and has {self.health} health.")

class Weapon():

    def __init__(self, attack_damage, mana_usage, price):
        self.attack_damage = attack_damage
        self.mana_usage = mana_usage
        self.price = price
        self.durability = durability

class Armour():

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Events():

    def __init__():
        self.place_name


    def grassland(self.place_name):
        print("You are in the grasslands! The enemys are weak here but give low gold")



shop = {1: ["Small Sword", 5], 2: ["Silver Sword", 20], 3: ["Massive Sword", 50], 4: ["Mega Ultimate Sword", 100]}

#Game start
print("Welcome to this adventure game\n\n*******************\n")
name = input("What is your name?")
print("Great!")

main_player = Player(name, 100, 100, 3, 0, 0, shop[1])

main_player.info()

#Travel
