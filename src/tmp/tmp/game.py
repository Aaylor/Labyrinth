#!/usr/bin/python3

import copy
from labyrinth import *

class game(object):

    def __init__(self, labyrinth_choice, **kwargs):
        """
        Initialise l'objet `game`... #TODO doc
        """
        if labyrinth_choice:
            self.game_labyrinth = generate_random_labyrinth(kwargs['width'],kwargs['height'])
        else:
            self.game_labyrinth = open_labyrinth(kwargs['filename'])
        self.player_position = copy.deepcopy(self.game_labyrinth.entry_position)

    def display(self):
        print(self.game_labyrinth)

if __name__ == "__main__":
    """
    TO READ
    a = game(True, width=PUT_INTEGER, height=PUT_INTEGER)   ->  Generate random labyrinth
    a = game(False, filename="filename.lab")    ->  Open a file
    """
    a = game(True, width=20, height=14)
    a.display()
    a.game_labyrinth.write_on_file("aa")

