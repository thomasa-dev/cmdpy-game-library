import library # importing custom library
import json
import os

# loot tables

data = json

class Game(): # INSTANCE class
    def __init__(self, name, version, author):
        self.name = name
        self.version = version
        self.author = author
    
    def main(self):
        os.system("cls")
        print("------------ CMDPY Demo ------------")
        print(f"Player Name: {self.Player_STATIC.name}")
        print(f"1 | Player Stats")
        print(f"2 | Player Skills")
        print(f"3 | Adventure")
        self.player_stats()
    
    def player_stats(self):
        player_stats = self.Player_STATIC.info["stats"]
        player_level = player_stats["level"]
        player_health = player_stats["health"]
        player_health_max = player_stats["health_max"]
        player_exp = player_stats["exp"]
        player_exp_max = player_stats["exp_max"]

        #os.system("cls")
        print("------------ CMDPY Demo ------------")
        print(f'Player Name: {self.Player_STATIC.name}')
        print(f'Player Health: {player_health} / {player_health_max}')
        print(f'Player Level: {player_level} | {player_exp} / {player_exp_max}')
    
    def setup(self):
        print("CMDPY | Loading player...")
        with open("items.json", "r") as file:
            items_data = json.load(file)
            items_list = []

        #library.load_data(items_data, "items.json")
        self.Player_STATIC = Player()
        library.load_data(self.Player_STATIC.info, "player_data.json")

        self.main()
        self.item_loader = library.Item_Loader(items_data, items_list)



class Player(library.Entity):
    def __init__(self):
        self.info = {
            "player_name": "Empty",
            "stats": {
                "health": 25,
                "health_max": 25,
                "level": 1,
                "skill_points": 0,
                "exp": 0,
                "exp_max": 500
            },
            "skills": {
                "foraging": 1,
                "lumbering": 1,
                "craftmanship": 1,
                "swordsmanship": 1,
                "forgery": 1,
                "archery": 1
            }
        }
        self.name = self.info["player_name"]
        super().__init__(self.name, self.info)
    
    def on_player_die(self):
        return
        # add whatever you want the player to do on death here



Game_INSTANCE = Game("CMDPY Demo", "v0.01-beta", "schizo rat#3149")
Game_INSTANCE.setup()