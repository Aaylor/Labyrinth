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
        self.labyrinthe = []
        self.player_pos = (0,0)
        self.end_pos = (0,0)
        read=_file.read()
        read=read.split('\n')
        if read[-1] == "":
            read = read[0:-1]
        self.length = len(read)-1
        for i, line in enumerate(read):
            self.labyrinthe.append([])
            for j, char in enumerate(line):
                self.labyrinthe[i].append(char)
                if (char == '0' and (j == 0 or j == len(line)-1) and (i&1 or i == 0 or i == self.length)):
                    self.end_pos = (i, j)
                if (char == '0' and (i == 0 or i == self.length)):
                    self.end_pos = (i, j)
                if (char == 'E'):
                    self.player_pos = (i, j)
        print(self.end_pos)
        _file.close()

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
                        elif '*' in j:
                            type_line = "|* "
                        else:
                            type_line = "|  "
                    print(type_line, end="")
                elif j == 'E':
                    if (i+1)&1:
                        type_line = " E "
                    else:
                        type_line = "E  "
                    print(type_line, end="")
                else:
                    if 'P' in j:
                        print(" P ", end="")
                    elif '*' in j:
                        print(" * ", end="")
                    else:
                        print("   ", end="")
            print("")

    def is_possible_move(self, direction, cur_pos):
        if cur_pos[0]&1 and cur_pos[0]+2 < (len(self.labyrinthe)-1):
            case = 2
        else:
            case = 1
        
        if direction == 'b':
            return  cur_pos[0]+case < len(self.labyrinthe) and \
                    not('1' in self.labyrinthe[cur_pos[0]+1][cur_pos[1]]) and \
                    (self.labyrinthe[cur_pos[0]+case][cur_pos[1]] != "1" or (cur_pos[0]+case)&1)
        if direction == 'h':
            return  not('1' in self.labyrinthe[cur_pos[0]-1][cur_pos[1]]) and \
                    (self.labyrinthe[cur_pos[0]-2][cur_pos[1]] != "1" or (cur_pos[0]-2)&1) and \
                    (cur_pos[0]-2 >= 0)
        if direction == 'g':
            return not('1' in self.labyrinthe[cur_pos[0]][cur_pos[1]]) and \
                    (self.labyrinthe[cur_pos[0]][cur_pos[1]-1] != "1" or cur_pos[0]&1)
        if direction == 'd':
            return not('1' in self.labyrinthe[cur_pos[0]][cur_pos[1]+1] == "1")

    def move(self, direction):
        if self.player_pos[0]&1 and self.player_pos[0]+2 < (len(self.labyrinthe)-1):
            case = 2
        else:
            case = 1
        
        if self.is_possible_move(direction, self.player_pos):
            self.labyrinthe[self.player_pos[0]][self.player_pos[1]] = self.labyrinthe[self.player_pos[0]][self.player_pos[1]][0]
            if d == 'b':
                self.player_pos = ( self.player_pos[0]+case, self.player_pos[1] )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
            if d == 'h':
                self.player_pos = ( self.player_pos[0]-2, self.player_pos[1] )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
            if d == 'g':
                self.player_pos = ( self.player_pos[0], self.player_pos[1]-1 )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
            if d == 'd':
                self.player_pos = ( self.player_pos[0], self.player_pos[1]+1 )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'

    def construct_tree(self, first_item, cur_tree):
        if cur_tree.value[0]&1 and cur_tree.value[0]+2 < (len(self.labyrinthe)-1):
            case = 2
        else:
            case = 1

        new_value = cur_tree.value
        if self.is_possible_move('b', new_value):
            cur_tree.add_son(Tree([new_value[0]+case, new_value[1]]), first_item)
        if self.is_possible_move('h', new_value):
            cur_tree.add_son(Tree([new_value[0]-2, new_value[1]]), first_item)
        if self.is_possible_move('g', new_value):
            cur_tree.add_son(Tree([new_value[0], new_value[1]-1]), first_item)
        if self.is_possible_move('d', new_value):
            cur_tree.add_son(Tree([new_value[0], new_value[1]+1]), first_item)

        for values in cur_tree.sons:
            self.construct_tree(first_item, values)

    def give_solution(self, liste, tree):
        for val in tree.sons:
            self.give_solution(liste, val)
        if tree.value == list(self.end_pos) or (list(self.end_pos) in liste):
            liste.append(tree.value)

    def display_solution(self, tree):
        liste = [] 
        self.give_solution(liste, tree)
        for value in liste:
            self.labyrinthe[value[0]][value[1]] += '*'
        self.display()

    def test(self):
        return self.player_pos == self.end_pos
    
if __name__ == "__main__":
    game = Game("test.txt")
    game.display()

    t = Tree(list(game.player_pos))
    game.construct_tree(t, t)
    #t.display_tree()

    game.display_solution(t)

    d = input("Move : ")
    while d != 'q':
        if d == 's':
            pass
        else:
            game.move(d)
        game.display()
        if game.test():
            print("You won !")
            break
        d = input("Move : ")
