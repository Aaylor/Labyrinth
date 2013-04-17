#!/usr/bin/python3

import copy
import player
import ast
from labyrinth import *
from utility.tree import *


class game(object):

    def __init__(self, labyrinth_choice, **kwargs):
        """Initialise l'objet `game`... #TODO doc
        """
        if labyrinth_choice:
            self.game_labyrinth = \
                generate_random_labyrinth(kwargs['width'], kwargs['height'])
        else:
            if 'loadgame' in kwargs.keys() and kwargs['loadgame']:
                self.load_game(kwargs['filename'])
            else:
                self.game_labyrinth = open_labyrinth(kwargs['filename'])
        if not 'loadgame' in kwargs.keys():
            self.player_position = copy.deepcopy(self.game_labyrinth.entry_position)
            self.player = player.Player(self.player_position,
                                        (self.game_labyrinth.height,
                                         self.game_labyrinth.width_on_odd_line))
            self.path_of_the_player = []
            self.way_list = []

    def display(self):
        """Affiche le labyrinthe"""
        print(self.game_labyrinth.disp_labyrinth(self.path_of_the_player))

    def case_deplacement(self, position, direction):
        """Calcul le déplacement autorisé selon la position et la direction
        données.
        
        Arguments :
        position    -- la position donnée (sous forme [x, y])
        direction   -- direction dans laquelle on doit aller
        """
        x, y = position
        if (((x == 0 or x == len(self.game_labyrinth.labyrinth) - 1)
            and not x & 1) or
            (x & 1 and ((x + 1 == len(self.game_labyrinth.labyrinth) - 1 and
                        direction == 'b') or
                        (x - 1 == 0 and direction == 'h')))):
            return 1
        return 2

    def is_a_possible_movement(self, position, direction):
        """Vérifie si le mouvement demandé à partir de la position et de la
        direction est possible, et renvoie True si il est possible, False
        sinon.

        Arguments :
        position    -- la position donnée (sous forme [x, y])
        direction   -- la direction souhaitée ('h', 'b', 'g', 'd')
        """
        if position == False :
            return False
        x, y = position
        if direction == 'b':
            case = self.case_deplacement(position, 'b')
            if ( (((x + case < len(self.game_labyrinth.labyrinth)) and
                    (y < len(self.game_labyrinth.labyrinth[x + case]) - 1 ^
                        (x == len(self.game_labyrinth.labyrinth) - 1 and
                    y < len(self.game_labyrinth.labyrinth[x + case]) - 1))) and
                    (not('1' in self.game_labyrinth.labyrinth[x + 1][y]) or
                    not(x & 1)) and
                    (self.game_labyrinth.labyrinth[x + case][y] != "1" or
                     (x + case) & 1)) ):
                return (position[0] + case, position[1])
            return False
        if direction == 'h':
            case = self.case_deplacement(position, 'h')
            if ( ((x - case >= 0 and x < len(self.game_labyrinth.labyrinth)) and
                    (y < len(self.game_labyrinth.labyrinth[x - case]) - 1 or
                        (x == len(self.game_labyrinth.labyrinth) - 1 and
                        (y < len(self.game_labyrinth[x - case]) - 1))) and
                    (not('1' in self.game_labyrinth.labyrinth[x - 1][y]) or
                    not(x & 1)) and
                    (self.game_labyrinth.labyrinth[x - case][y] != "1" or
                     (x - case) & 1))):
                return (position[0] - case, position[1])
            return False
        if direction == 'g':
            if ( ((y - 1) >= 0 and x < len(self.game_labyrinth.labyrinth)) and \
                not('1' in self.game_labyrinth.labyrinth[x][y]) and \
                (self.game_labyrinth.labyrinth[x][y - 1] != "1" or x & 1)):
                return (position[0], position[1] - 1)
            return False
        if direction == 'd':
            if ( (x < len(self.game_labyrinth.labyrinth) and \
                    (y + 1) < len(self.game_labyrinth.labyrinth[x])) and \
                not('1' in self.game_labyrinth.labyrinth[x][y + 1])):
                return (position[0], position[1] + 1)
            return False

    def move(self, direction):
        """Bouge le pion du joueur dans la direction donnée si il est possible
        d'effectuer le mouvement.

        Argument:
        direction   -- la direction souhaitée par le joueur
        """
        if self.is_a_possible_movement(self.player_position, direction):
            self.game_labyrinth.\
                labyrinth[self.player_position[0]][self.player_position[1]] =\
                (self.game_labyrinth.labyrinth
                    [self.player_position[0]]
                    [self.player_position[1]][0])
            if direction == 'b':
                case = self.case_deplacement(self.player_position, direction)
                self.player_position = (self.player_position[0] + case,
                                        self.player_position[1])
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
                self.path_of_the_player.append(list(self.player_position))
            if direction == 'h':
                case = self.case_deplacement(self.player_position, direction)
                self.player_position = (self.player_position[0] - case,
                                        self.player_position[1])
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
                self.path_of_the_player.append(list(self.player_position))
            if direction == 'g':
                self.player_position = (self.player_position[0],
                                        self.player_position[1] - 1)
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
                self.path_of_the_player.append(list(self.player_position))
            if direction == 'd':
                self.player_position = (self.player_position[0],
                                        self.player_position[1] + 1)
                self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
                self.path_of_the_player.append(list(self.player_position))

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
        """Affiche la solution sur le labyrinthe"""
        tree_from_current_position = Tree(list(self.player_position))
        self.__construct_tree(tree_from_current_position,
                              tree_from_current_position)
        
        self.way_list = []
        self.__give_solution(self.way_list, tree_from_current_position)

        for value in self.way_list:
            self.game_labyrinth.labyrinth[value[0]][value[1]] += chr(9632)

    def undisplay_solution(self):
        """Enlève la solution du labyrinthe"""
        for value in self.way_list:
            if 'P' not in self.game_labyrinth.labyrinth[value[0]][value[1]]:
                self.game_labyrinth.labyrinth[value[0]][value[1]] =\
                    self.game_labyrinth.labyrinth[value[0]][value[1]][0]

    def is_at_exit_point(self):
        return self.player_position == self.game_labyrinth.exit_position

    def save_game(self, filename):
        try:
            _file = open(filename, "w")
        except IOError:
            return False

        _file.write("height=" + str(self.game_labyrinth.height) + "\n")
        for i in self.game_labyrinth.labyrinth:
            _file.write("".join(map(lambda x : '1' if '1' in x else
                                list(map((lambda y : '0' if '0' in x else 'E'), [x]))[0], i)) + "\n")
        _file.write("player_pos=" + str(self.player_position[0]) + "," +
                    str(self.player_position[1]) + "\n")
        #player_pos use here... maybe write Player object instead ?
        _file.write("path=" + str(self.path_of_the_player))

    def load_game(self, filename):
        try:
            _file = open(filename, "r")
        except IOError:
            return False

        info = _file.read().split("\n")
        if not info[-1]:
            del info[-1]
        height = int((info[0].split("="))[1]) + 1
        self.game_labyrinth = read_labyrinth(info[1:height+1])
        self.player_position = ast.literal_eval((info[height+1].split("="))[1])
        self.game_labyrinth.labyrinth[self.player_position[0]][self.player_position[1]] += 'P'
        #ast.literal_eval, this function evaluate string and return list,
        #tuple or every literal evaluation
        self.path_of_the_player = ast.literal_eval((info[-1].split("="))[1])

if __name__ == "__main__":
    """
    TO READ
    a = game(True, width=PUT_INTEGER, height=PUT_INTEGER)
        ->  Generate random labyrinth
    a = game(False, filename="filename.lab")
        ->  Open a file
    a = game(False, filename="filename.sav", loadgame=True)
    """
    #a = game(True, width=20, height=14)
    #a = game(False, filename="rand_lab.lab")
    a = game(False, filename="test.sav", loadgame=True)
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
        if d == 'sa':
            a.save_game("test.sav")
        if d == 'lo':
            a.load_game("test.sav")
        a.move(d)
