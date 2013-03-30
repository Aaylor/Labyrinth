#!/usr/bin/python3

import random
from tree import *
from laby import *

class generate_laby(object):

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.vertical_wall = [[True for i in range(width+1)] for j in range(height)]
        self.horizontal_wall = [[True for i in range(width)] for j in range(height+1)]
        self.enter = [0,0]
        self.labyrinthe = self.init_labyrinthe()
        self.create_labyrinthe()

    def init_labyrinthe(self):
        liste = []
        cpt = 0
        for i in range(self.height):
            liste.append([])
            for j in range(self.width):
                liste[i].append(cpt)
                cpt += 1
        return liste

    def create_labyrinthe(self):
        while not self.end_of_init():
            random_choice = random.randint(0,1)
            if random_choice == 0:
                remove_random_wall = [random.randint(0,self.height-1), random.randint(1,self.width-1)]
                while not self.vertical_wall[remove_random_wall[0]][remove_random_wall[1]]:
                    remove_random_wall = [random.randint(0,self.height-1), random.randint(1,self.width-1)]
                new_value = self.labyrinthe[remove_random_wall[0]][remove_random_wall[1]]
                old_value = self.labyrinthe[remove_random_wall[0]][remove_random_wall[1]-1]
                if new_value != old_value:
                    self.vertical_wall[remove_random_wall[0]][remove_random_wall[1]] = False
                    if old_value < new_value:
                        new_value, old_value = old_value, new_value
                    self.change_value(old_value, new_value)
            else:
                remove_random_wall = [random.randint(1,self.height-1), random.randint(0,self.width-1)]
                while not self.horizontal_wall[remove_random_wall[0]][remove_random_wall[1]]:
                    remove_random_wall = [random.randint(1,self.height-1), random.randint(0,self.width-1)]
                new_value = self.labyrinthe[remove_random_wall[0]][remove_random_wall[1]]
                old_value = self.labyrinthe[remove_random_wall[0]-1][remove_random_wall[1]]
                if new_value != old_value:
                    self.horizontal_wall[remove_random_wall[0]][remove_random_wall[1]] = False
                    if old_value < new_value:
                        new_value, old_value = old_value, new_value
                    self.change_value(old_value, new_value)
        self.create_enter_and_exit()

    def create_enter_and_exit(self):
        enter_already_placed = False
        for i in range(2):
            random_choice = random.randint(0,1)
            if i&1:
                x = random.randrange(1, len(self.vertical_wall)-2, 2)
                y = random.choice([0, len(self.vertical_wall[x])-1])
                while self.vertical_wall[x][y] != True:
                    x = random.randrange(1, len(self.vertical_wall)-2, 2)
                    y = random.choice([0, len(self.vertical_wall[x])-1])
                self.vertical_wall[x][y] = False
                if (not enter_already_placed and random.randint(0,1)==1) or (i == 1 and not enter_already_placed):
                    self.vertical_wall[x][y] = 'E'
                    enter_already_placed = True
            else:
                x = random.choice([0, len(self.horizontal_wall)-1])
                y = random.randint(1, len(self.horizontal_wall[x])-2)
                while self.horizontal_wall[x][y] != True:
                    x = random.choice([0, len(self.horizontal_wall)-1])
                    y = random.randint(1, len(self.horizontal_wall[x])-2)
                self.horizontal_wall[x][y] = False
                if (not enter_already_placed and random.randint(0,1)==1) or (i == 1 and not enter_already_placed):
                    self.horizontal_wall[x][y] = 'E'
                    enter_already_placed = True

    def change_value(self, old_value, new_value):
        for i in range(self.height):
            for j in range(self.width):
                if self.labyrinthe[i][j] == old_value:
                    self.labyrinthe[i][j] = new_value

    def end_of_init(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.labyrinthe[i][j] != 0:
                    return False
        return True

    def save_to_file(self):
        _file = open("rand_lab.txt", 'w')
        cpt_hor = 0
        cpt_ver = 0

        for i in range((self.width*2)+1):
            if i&1 and cpt_ver < len(self.vertical_wall):
                a = "".join(map(lambda x: 'c' if x is True else list(map((lambda y: 'd' if not y else 'e'),[x]))[0], self.vertical_wall[cpt_ver]))
                print(a)
                _file.write('\n')
                cpt_ver += 1
            elif not i&1 and cpt_hor < len(self.horizontal_wall):
                for value in self.horizontal_wall[cpt_hor]:
                    if value == True:
                        _file.write('1')
                    elif value == 'E':
                        _file.write('E')
                    else:
                        _file.write('0')
                _file.write('\n')
                cpt_hor += 1

if __name__ == "__main__":
    l = generate_laby(20, 14)
    l.save_to_file()

    lab = Game("rand_lab.txt")
    lab.display()
