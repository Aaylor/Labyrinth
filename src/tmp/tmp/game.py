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

    def case_deplacement(self, position, direction):
        x, y = position
        if  ((x == 0 or x == len(self.game_labyrinth.labyrinth)-1) and not x&1) or \
            (x&1 and ((x+1 == len(self.game_labyrinth.labyrinth)-1 and direction == 'b') or \
            (x-1 == 0 and direction == 'h'))):
            return 1
        return 2
    
    def is_a_possible_movement(self, position, direction):
        x, y = position
        if direction == 'b':
            case = self.case_deplacement(position, 'b')
            return  ((x+case < len(self.game_labyrinth.labyrinth)) and (y < len(self.game_labyrinth.labyrinth[x+case])-1 ^ \
                    (x == len(self.game_labyrinth.labyrinth)-1 and y < len(self.game_labyrinth.labyrinth[x+case])-1))) and \
                    (not('1' in self.game_labyrinth.labyrinth[x+1][y]) or \
                    not(x&1)) and \
                    (self.game_labyrinth.labyrinth[x+case][y] != "1" or (x+case)&1)
        if direction == 'h':
            case = self.case_deplacement(position, 'h')
            return  (x-case >= 0) and (y < len(self.game_labyrinth.labyrinth[x-case])-1 or \
                    (x == len(self.game_labyrinth.labyrinth)-1 and y < len(self.game_labyrinth[x-case])-1)) and \
                    (not('1' in self.game_labyrinth.labyrinth[x-1][y]) or \
                    not(x&1)) and \
                    (self.game_labyrinth.labyrinth[x-case][y] != "1" or (x-case)&1)
        if direction == 'g':
            return  y-1 >= 0 and\
                    not('1' in self.game_labyrinth.labyrinth[x][y]) and \
                    (self.game_labyrinth.labyrinth[x][y-1] != "1" or x&1)
        if direction == 'd':
            return  y+1 < len(self.game_labyrinth.labyrinth[x]) and \
                    not('1' in self.game_labyrinth.labyrinth[x][y+1] == "1")
    
    def move(self, direction):
        if self.is_a_possible_movement(self.player_position, direction):
            self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] = \
                    self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]][0]
            if d == 'b':
                print("b")
                case = self.case_deplacement(self.player_position, d)
                self.player_position = ( self.player_position[0]+case, self.player_position[1] )
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
            if d == 'h':
                print("h")
                case = self.case_deplacement(self.player_position, d)
                self.player_position = ( self.player_position[0]-case, self.player_position[1] )
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
            if d == 'g':
                print("g")
                self.player_position = ( self.player_position[0], self.player_position[1]-1 )
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
            if d == 'd':
                print("d")
                self.player_position = ( self.player_position[0], self.player_position[1]+1 )
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'

if __name__ == "__main__":
    """
    TO READ
    a = game(True, width=PUT_INTEGER, height=PUT_INTEGER)   ->  Generate random labyrinth
    a = game(False, filename="filename.lab")    ->  Open a file
    """
    #a = game(True, width=20, height=14)
    a = game(False, filename="rand_lab.txt")
    #a.game_labyrinth.write_on_file("b")
    while True:
        a.display()
        print(a.game_labyrinth.labyrinth)
        print(a.player_position)
        d = input("Move : ")
        if d == 'q':
            break
        a.move(d)
        

