# Made by a schizophrenic twat

# How the code is formatted:
# all classes have capital letters (eg. Game, or Player)
# all variables have lowercase letters (eg. data, or stats)
# constantly running classes (eg. Game) will be named Class_INSTANCE (eg. Game_INSTANCE)

from array import array
import json
from random import randint # for saving and loading data


debug = False # for debugging

# Functions

def save_data(data=json, file=None): # for saving data such as player data
    with open(file, 'w') as file_handle:
        json.dump(data, file_handle)

    if debug: print(f"Saved data to {file_handle.name}")

def load_data(data=json, file=None): # for loading data such as player data
    with open(file, 'r') as file_handle:
        data = json.load(file_handle)

    if debug: print(str(data))


# Classes

class Loot_Table(): # for loot drops
    def __init__(self, loot=array):
        self.loot = loot
    
    def roll(self):
        possible_drop_count = -1
        for x in self.loot:
            possible_drop_count += 1

        selected = self.loot[randint(0, possible_drop_count)]
        print(f"CMDPY | Selected Item: {selected}")



class Entity(): # STATIC class
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
    
    def death(self, loot_table=Loot_Table):
        loot_table.roll()



class Item(): # STATIC class
    def __init__(self, name, category, stats=json):
        self.name = name,
        self.category = category
        self.stats = json