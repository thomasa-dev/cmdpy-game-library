import json
import library # importing custom library

# loot tables



class Game(): # INSTANCE class
    def __init__(self, name, version, author, player_class):
        self.name = name
        self.version = version
        self.author = author
    
    def setup(self):
        return



class Player(library.Entity):
    def __init__(self, name, stats=json):
        super().__init__(name, stats)

        self.name = name
        self.stats = stats
    
    def on_player_die(self):
        super().death(25, player_loot_table)
        # add whatever you want the player to do on death here



Player_STATIC = Player("Developer Account", {"name": "Developer Account"})
Game_INSTANCE = Game("CMDPY Demo", "v0.01-beta", "schizo rat#3149", Player_STATIC)