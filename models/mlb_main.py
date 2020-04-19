import progressbar

from models.league import League
from models.mlb.games import *
from models.mlb.rankings import *
from models.mlb.batting import *

class MLB(League):
    def __init__(self):
        super(MLB).__init__()

    def fill_table(self, engine):
        print("--- Filling database with game statistics ---")
        fill_game_statistics(engine)
        print("--- Filling database with rankings ---")
        fill_rankings(engine)
        print("--- Filling database with batting statistics ---")
        fill_batting_statistics(engine)
