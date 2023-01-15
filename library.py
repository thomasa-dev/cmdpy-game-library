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
    def __init__(self, name, description, category, manufacturer, level, damage, health_gain):
        self.name = name
        self.description = description
        self.category = category
        self.manufacturer = manufacturer
        self.level = level
        self.damage = damage
        self.health_gain = health_gain

class Item_Loader(): # STATIC class
    def __init__(self, items_data = json, items_list=array):
        for item in items_data:

            items_list.append(Item(
                item.get('name'),
                item.get('description'),
                item.get('category'),
                item.get('manufacturer'),
                item.get('level'),
                item.get('damage'),
                item.get('health_gain')
            ))
        
        print(items_list)