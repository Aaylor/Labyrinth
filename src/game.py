#!/usr/bin/python3

import copy
from labyrinth import *
from tree import *


class game(object):

    def __init__(self, labyrinth_choice, **kwargs):
        """Initialise l'objet `game`... #TODO doc
        """
        if labyrinth_choice:
            self.game_labyrinth = \
                generate_random_labyrinth(kwargs['width'], kwargs['height'])
        else:
            self.game_labyrinth = open_labyrinth(kwargs['filename'])
        self.player_position = copy.deepcopy(self.game_labyrinth.entry_position)

    def display(self):
        print(self.game_labyrinth)

    def case_deplacement(self, position, direction):
        x, y = position
        if (((x == 0 or x == len(self.game_labyrinth.labyrinth) - 1)
            and not x & 1) or
            (x & 1 and ((x + 1 == len(self.game_labyrinth.labyrinth) - 1 and
                        direction == 'b') or
                        (x - 1 == 0 and direction == 'h')))):
            return 1
        return 2

    def is_a_possible_movement(self, position, direction):
        x, y = position
        if direction == 'b':
            case = self.case_deplacement(position, 'b')
            return (((x + case < len(self.game_labyrinth.labyrinth)) and
                    (y < len(self.game_labyrinth.labyrinth[x + case]) - 1 ^
                        (x == len(self.game_labyrinth.labyrinth) - 1 and
                    y < len(self.game_labyrinth.labyrinth[x + case]) - 1))) and
                    (not('1' in self.game_labyrinth.labyrinth[x + 1][y]) or
                    not(x & 1)) and
                    (self.game_labyrinth.labyrinth[x + case][y] != "1" or
                    (x + case) & 1))
        if direction == 'h':
            case = self.case_deplacement(position, 'h')
            return ((x - case >= 0) and
                    (y < len(self.game_labyrinth.labyrinth[x - case]) - 1 or
                        (x == len(self.game_labyrinth.labyrinth) - 1 and
                        (y < len(self.game_labyrinth[x - case]) - 1))) and
                    (not('1' in self.game_labyrinth.labyrinth[x - 1][y]) or
                    not(x & 1)) and
                    (self.game_labyrinth.labyrinth[x - case][y] != "1" or
                        (x - case) & 1))
        if direction == 'g':
            return (y - 1) >= 0 and \
                not('1' in self.game_labyrinth.labyrinth[x][y]) and \
                (self.game_labyrinth.labyrinth[x][y - 1] != "1" or x & 1)
        if direction == 'd':
            return (y + 1) < len(self.game_labyrinth.labyrinth[x]) and \
                not('1' in self.game_labyrinth.labyrinth[x][y + 1] == "1")

    def move(self, direction):
        if self.is_a_possible_movement(self.player_position, direction):
            self.game_labyrinth.\
                labyrinth[self.player_position[0]][self.player_position[1]] =\
                (self.game_labyrinth.labyrinth
                    [self.player_position[0]]
                    [self.player_position[1]][0])
            if d == 'b':
                case = self.case_deplacement(self.player_position, d)
                self.player_position = (self.player_position[0] + case,
                                        self.player_position[1])
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
            if d == 'h':
                case = self.case_deplacement(self.player_position, d)
                self.player_position = (self.player_position[0] - case,
                                        self.player_position[1])
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
            if d == 'g':
                self.player_position = (self.player_position[0],
                                        self.player_position[1] - 1)
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
            if d == 'd':
                self.player_position = (self.player_position[0],
                                        self.player_position[1] + 1)
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'

    def __construct_tree(self, first_item, current_tree):
        tree_position = current_tree.value
        if self.is_a_possible_movement(tree_position, 'b'):
            case = self.case_deplacement(tree_position, 'b')
            current_tree.add_son(Tree([tree_position[0] + case,
                                       tree_position[1]]), first_item)
        if self.is_a_possible_movement(tree_position, 'h'):
            case = self.case_deplacement(tree_position, 'h')
            current_tree.add_son(Tree([tree_position[0] - case,
                                       tree_position[1]]), first_item)
        if self.is_a_possible_movement(tree_position, 'g'):
            current_tree.add_son(Tree([tree_position[0], tree_position[1] - 1]),
                                      first_item)
        if self.is_a_possible_movement(tree_position, 'd'):
            current_tree.add_son(Tree([tree_position[0], tree_position[1] + 1]),
                                      first_item)

        for tree_sons in current_tree.sons:
            self.__construct_tree(first_item, tree_sons)

    def __give_solution(self, liste, tree):
        for values in tree.sons:
            if list(self.game_labyrinth.exit_position) not in liste:
                self.__give_solution(liste, values)
        if (tree.value == list(self.game_labyrinth.exit_position) or
            (list(self.game_labyrinth.exit_position) in liste)):
            liste.append(tree.value)

    def display_solution(self):
        tree_from_current_position = Tree(list(self.player_position))
        self.__construct_tree(tree_from_current_position,
                              tree_from_current_position)
        
        self.way_list = []
        self.__give_solution(self.way_list, tree_from_current_position)

        for value in self.way_list:
            self.game_labyrinth.labyrinth[value[0]][value[1]] += chr(9632)

    def undisplay_solution(self):
        for value in self.way_list:
            if 'P' not in self.game_labyrinth.labyrinth[value[0]][value[1]]:
                self.game_labyrinth.labyrinth[value[0]][value[1]] =\
                    self.game_labyrinth.labyrinth[value[0]][value[1]][0]

if __name__ == "__main__":
    """
    TO READ
    a = game(True, width=PUT_INTEGER, height=PUT_INTEGER)
        ->  Generate random labyrinth
    a = game(False, filename="filename.lab")
        ->  Open a file
    """
    a = game(True, width=20, height=14)
    #a = game(False, filename="rand_lab.txt")
    #a.game_labyrinth.write_on_file("b")
    while True:
        a.display()
        d = input("Move : ")
        if d == 's':
            a.display_solution()
        if d == 'u':
            a.undisplay_solution()
        if d == 'q':
            break
        a.move(d)
