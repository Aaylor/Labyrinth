#!/usr/bin/python3

import tkinter
from tree import *

class Game:
    def __init__(self, filename):
        try:
            _file = open(filename, 'r')
        except IOError:
            print("File not found...")
            exit(1)
        bool_enter, bool_exit = False, False
        self.labyrinthe = []
        self.player_pos, self.end_pos = (0,0), (0,0)
        read=_file.read()
        read=read.split('\n')
        if read[-1] == "":
            read = read[0:-1]
        self.length = len(read)-1
        print(len(read)-1, len(read[0])-1)
        for i, line in enumerate(read):
            self.labyrinthe.append([])
            for j, char in enumerate(line):
                self.labyrinthe[i].append(char)
                """
                if  ((char == '0' and (j == 0 or j == len(line)-1) and (i&1 or i == 0 or i == self.length))) or \
                    (char == '0' and (i == 0 or i == self.length)):
                """
                if char == '0' and ((i == 0 or i == self.length) or (i&1 and (j == 0 or j== len(line)-1))):
                    print(char == '0', i == 0 or i == self.length, i&1 and (j == 0 or j == len(line)-1))
                    self.end_pos = (i, j)
                    if bool_exit:
                        print("Exit already exist...")
                        exit(1)
                    bool_exit = True
                if (char == 'E'):
                    self.player_pos = (i, j)
                    if bool_enter:
                        print("Enter already exist...")
                        exit(1)
                    bool_enter = True
        _file.close()
        if not bool_exit or not bool_enter:
            print("No entry or no exit...")
            exit(1)


    def display(self):
        print(self.player_pos)
        for i, k in enumerate(self.labyrinthe):
            for j in k:
                if '1' in j:
                    if (i+1)&1:
                        type_line = "---"
                    else:
                        if 'P' in j:
                            type_line = "|P "
                        elif chr(9632) in j:
                            type_line = "|"+chr(9632)+" "
                        elif chr(9829) in j:
                            type_line = "|"+chr(9829)+" "
                        else:
                            type_line = "|  "
                    print(type_line, end="")
                elif j == 'E':
                    if (i+1)&1:
                        if '*' in j:
                            type_line = " E*"
                        else:
                            type_line = " E "
                    else:
                        if '*' in j:
                            type_line = "E* "
                        else:
                            type_line = "E  "
                    print(type_line, end="")
                else:
                    if 'P' in j:
                        print(" P ", end="")
                    elif chr(9632) in j:
                        print(" "+chr(9632)+" ", end="")
                    elif chr(9829) in j:
                        print(" "+chr(9829)+" ", end="")
                    else:
                        print("   ", end="")
            print("")

    def case_deplacement(self, cur_pos, direction):
        if  ((cur_pos[0] == 0 or cur_pos[0] == len(self.labyrinthe)-1) and not cur_pos[0]&1) or \
            (cur_pos[0]&1 and ((cur_pos[0]+1 == len(self.labyrinthe)-1 and direction == 'b') or \
            (cur_pos[0]-1 == 0 and direction == 'h'))):
            return 1
        return 2

    def is_possible_move(self, direction, cur_pos):
        if direction == 'b':
            case = self.case_deplacement(cur_pos, 'b')
            return  ((cur_pos[0]+case < len(self.labyrinthe)) and (cur_pos[1] < len(self.labyrinthe[cur_pos[0]+case])-1 ^ \
                    (cur_pos[0] == len(self.labyrinthe)-1 and cur_pos[1] < len(self.labyrinthe[cur_pos[0]+case])-1))) and \
                    (not('1' in self.labyrinthe[cur_pos[0]+1][cur_pos[1]]) or \
                    not(cur_pos[0]&1)) and \
                    (self.labyrinthe[cur_pos[0]+case][cur_pos[1]] != "1" or (cur_pos[0]+case)&1)
        if direction == 'h':
            case = self.case_deplacement(cur_pos, 'h')
            return  (cur_pos[0]-case >= 0) and (cur_pos[1] < len(self.labyrinthe[cur_pos[0]-case])-1 or \
                    (cur_pos[0] == len(self.labyrinthe)-1 and cur_pos[1] < len(self.labyrinthe[cur_pos[0]-case])-1)) and \
                    (not('1' in self.labyrinthe[cur_pos[0]-1][cur_pos[1]]) or \
                    not(cur_pos[0]&1)) and \
                    (self.labyrinthe[cur_pos[0]-case][cur_pos[1]] != "1" or (cur_pos[0]-case)&1)
        if direction == 'g':
            return  cur_pos[1]-1 >= 0 and\
                    not('1' in self.labyrinthe[cur_pos[0]][cur_pos[1]]) and \
                    (self.labyrinthe[cur_pos[0]][cur_pos[1]-1] != "1" or cur_pos[0]&1)
        if direction == 'd':
            return  cur_pos[1]+1 < len(self.labyrinthe[cur_pos[0]]) and \
                    not('1' in self.labyrinthe[cur_pos[0]][cur_pos[1]+1] == "1")

    def move(self, direction):
        if self.is_possible_move(direction, self.player_pos):
            self.labyrinthe[self.player_pos[0]][self.player_pos[1]] = self.labyrinthe[self.player_pos[0]][self.player_pos[1]][0]
            if d == 'b':
                case = self.case_deplacement(self.player_pos, d)
                self.player_pos = ( self.player_pos[0]+case, self.player_pos[1] )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
            if d == 'h':
                case = self.case_deplacement(self.player_pos, d)
                self.player_pos = ( self.player_pos[0]-case, self.player_pos[1] )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
            if d == 'g':
                self.player_pos = ( self.player_pos[0], self.player_pos[1]-1 )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
            if d == 'd':
                self.player_pos = ( self.player_pos[0], self.player_pos[1]+1 )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'

    def construct_tree(self, first_item, cur_tree):
        new_value = cur_tree.value
        if self.is_possible_move('b', new_value):
            case = self.case_deplacement(cur_tree.value, 'b')
            cur_tree.add_son(Tree([new_value[0]+case, new_value[1]]), first_item)
        if self.is_possible_move('h', new_value):
            case = self.case_deplacement(cur_tree.value, 'h')
            cur_tree.add_son(Tree([new_value[0]-case, new_value[1]]), first_item)
        if self.is_possible_move('g', new_value):
            cur_tree.add_son(Tree([new_value[0], new_value[1]-1]), first_item)
        if self.is_possible_move('d', new_value):
            cur_tree.add_son(Tree([new_value[0], new_value[1]+1]), first_item)

        for values in cur_tree.sons:
            self.construct_tree(first_item, values)

    def give_solution(self, liste, tree, indent=0):
        for val in tree.sons:
             if list(self.end_pos) not in liste:
                self.give_solution(liste, val, indent+1)
        if tree.value == list(self.end_pos) or (list(self.end_pos) in liste):
            liste.append(tree.value)

    def display_solution(self, tree):
        liste = [] 
        self.give_solution(liste, tree)
        for value in liste:
            #self.labyrinthe[value[0]][value[1]] += chr(9829)
            self.labyrinthe[value[0]][value[1]] += chr(9632)
        self.display()

    def test(self):
        return self.player_pos == self.end_pos
    
if __name__ == "__main__":
    game = Game("rand_lab.txt")
    game.display()

    t = Tree(list(game.player_pos))
    game.construct_tree(t, t)
    #t.display_tree()

    d = input("Move : ")
    while d != 'q':
        if d == 's':
            game.display_solution(t)
        else:
            game.move(d)
        game.display()
        if game.test():
            print("You won !")
            break
        d = input("Move : ")
