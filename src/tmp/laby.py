#!/usr/bin/python3

import tkinter

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
                    else:
                        print("   ", end="")
            print("")

    def move(self, direction):
        if self.player_pos[0]&1 and self.player_pos[0]+2 < (len(self.labyrinthe)-1):
            case = 2
        else:
            case = 1
        if d == 'b':
            if not ('1' in self.labyrinthe[self.player_pos[0]+1][self.player_pos[1]]):
                if self.labyrinthe[self.player_pos[0]+case][self.player_pos[1]] != "1" or (self.player_pos[0]+case)&1:
                    self.labyrinthe[self.player_pos[0]][self.player_pos[1]] = self.labyrinthe[self.player_pos[0]][self.player_pos[1]][0]
                    self.player_pos = ( self.player_pos[0]+case, self.player_pos[1] )
                    self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
        if d == 'h':
            if not('1' in self.labyrinthe[self.player_pos[0]-1][self.player_pos[1]]):
                if self.labyrinthe[self.player_pos[0]-2][self.player_pos[1]] != "1" or (self.player_pos[0]-2)&1:
                    self.labyrinthe[self.player_pos[0]][self.player_pos[1]] = self.labyrinthe[self.player_pos[0]][self.player_pos[1]][0]
                    self.player_pos = ( self.player_pos[0]-2, self.player_pos[1] )
                    self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
        if d == 'g':
            if not ('1' in self.labyrinthe[self.player_pos[0]][self.player_pos[1]]):
                if (self.labyrinthe[self.player_pos[0]][self.player_pos[1]-1] != "1" or self.player_pos[0]&1):
                    self.labyrinthe[self.player_pos[0]][self.player_pos[1]] = self.labyrinthe[self.player_pos[0]][self.player_pos[1]][0]
                    self.player_pos = ( self.player_pos[0], self.player_pos[1]-1 )
                    self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'
        if d == 'd':
            if self.labyrinthe[self.player_pos[0]][self.player_pos[1]+1] != "1":
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] = self.labyrinthe[self.player_pos[0]][self.player_pos[1]][0]
                self.player_pos = ( self.player_pos[0], self.player_pos[1]+1 )
                self.labyrinthe[self.player_pos[0]][self.player_pos[1]] += 'P'

    def test(self):
        return self.player_pos == self.end_pos
    
if __name__ == "__main__":
    game = Game("test.txt")
    game.display()

    d = input("Move : ")
    while d != 'q':
        game.move(d)
        game.display()
        if game.test():
            print("You won !")
            break
        d = input("Move : ")
