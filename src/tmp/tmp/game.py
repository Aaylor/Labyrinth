#!/usr/bin/python3

import copy
from labyrinth import *

class game(object):

    def __init__(self, labyrinth_choice):
        """
        Initialise l'objet `game`... #TODO doc
        """
        if labyrinth_choice:
            self.game_labyrinth = generate_random_labyrinth(10,10)
        else:
            self.game_labyrinth = open_labyrinthe()
        self.player_position = copy.deepcopy(self.game_labyrinth.entry_position)

    def display(self):
        print(self.game_labyrinth)

if __name__ == "__main__":
   a = game(True)
   a.display()

