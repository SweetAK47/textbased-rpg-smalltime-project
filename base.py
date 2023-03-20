### branch this later or whatever
import time
import random
import sys
import os
from random import randint


items = ["axe", "bow", "arrow"]

enemyAI = ["goblin", "orc", "troll", "dragon"]

baseplrdamage = 10
baselvlupxp = 100
lvlupxp = baselvlupxp
levelbuff = 1

class character:
    def __init__(self):
        self.name = ""
        self.hp = 100
        self.protection = 0
        self.equippedweapon = ""
        self.mp = 100
        self.lvl = 1
        self.xp = 0
        self.items = []
        self.unlockedmagic = []
        self.location = "forest"

# if character.xp >= lvlupxp:
def levelups():
    character.lvl += 1
    levelbuff = 0.25*character.lvl
    character.xp = 0
    character.hp = 100 * levelbuff
    character.mp = 100 * levelbuff
    print("You leveled up! You are now level", character.lvl, "!")
    mainui()

class enemy:
    def __init__(self):
        self.name = [random.choice(enemyAI)]
        self.hp = 0 ## add enemy files to get hp
        self.damage = [random.randint(1, 50)]
        self.loot = [random.choice(items)]

def mainui():
    print("\nHealth: ",character.hp, "\nMP: ",character.MP, "\nLevel: ",character.lvl, "\nXP: ",character.xp)
    print("""
    1) Explore
    2) Travel
    3) Inventory
    4) Save
    5) Quit
    """)
    choice = input("What would you like to do? ")

def start():
    directions = ["1", "2"]
    userInput = ""
    while userInput not in directions:
        print("""\n
        1) Go to the village
        2) Explore the forest""")
        userInput = input("\nWhat would you like to do? ")
        if userInput == "1":
            introvillage()
        elif userInput == "2":
            introforest()
        else:
            print("Invalid input")

def introforest():
    directions = ["1", "2"]
    print("You decide to explore the forest. You walk for a while and see a small cave in the distance. \nYou have a bad feeling about this, do you enter the cave or continue exploring the forest?")
    userInput = ""
    while userInput not in directions:
        print("""\n
        1) Enter the cave
        2) Continue exploring the forest
        3) Go back""")
        userinput = input("\nWhat would you like to do? ")
        if userInput == "1":
            introcave()
        elif userInput == "2":
            introdeepforest()
        elif userInput == "3":
            print("\nYou decide to go back to where you woke up and walk to the village.")
            introvillage()
        else:
            print("Invalid input")

def introdeepforest():
    return # add later

def introcave():
    return # add later

def introvillage():
    return


if __name__ == "__main__":
    while True:
        character.name = input("Enter character name: ")
        print("You wake up in a forest. You have no idea how you got here, you look around and see a small village in the distance.", "\nDo you go to the village or explore the forest?")
        start()




