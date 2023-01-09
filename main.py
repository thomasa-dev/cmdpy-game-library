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
    
    def setup(self):
        print("CMDPY | Loading player...")
        self.Player_STATIC = Player()
        library.load_data(self.Player_STATIC.stats, "player_data.json")

        self.main()



class Player(library.Entity):
    def __init__(self):
        self.stats = {
            "player_name": "Empty",
            "stats": {
                "health": 25,
                "health_max": 25,
                "level": 1,
                "skill_points": 0,
                "xp": 0,
                "xp_max": 500
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
        self.name = self.stats["player_name"]
        super().__init__(self.name, self.stats)
    
    def on_player_die(self):
        return
        # add whatever you want the player to do on death here



Game_INSTANCE = Game("CMDPY Demo", "v0.01-beta", "schizo rat#3149")
Game_INSTANCE.setup()