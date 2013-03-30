#!/usr/bin/python3

import random

class labyrinth(object):
    """
    Classe mère ...
    """
    
    def __init__(self, width_on_odd_line, height):
        self.width_on_odd_line = width_on_odd_line
        self.width_on_even_line = width_on_odd_line + 1
        self.height = height

    def __str__(self):
        display_labyrinth = ""
        print(self.labyrinth)
        for i, k in enumerate(self.labyrinth):
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
                    display_labyrinth += type_line
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
                    display_labyrinth += type_line
                else:
                    if 'P' in j:
                        display_labyrinth += " P "
                    elif chr(9632) in j:
                        display_labyrinth += " "+chr(9632)+" "
                    elif chr(9829) in j:
                        display_labyrinth += " "+chr(9829)+" "
                    else:
                        display_labyrinth += "   "
            display_labyrinth += "\n"
        return display_labyrinth
    


class generate_random_labyrinth(labyrinth):
    """
    Classe fille ... RANDOM
    """

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.vertical_wall = [[True for i in range(width+1)] for j in range(height)]
        self.horizontal_wall = [[True for i in range(width)] for j in range(height+1)]
        self.entry_position = None
        self.exit_position = None
        self.labyrinth = []
        self.__create_labyrinth()

    def __create_labyrinth(self):
        tmp_labyrinth = [[(j + (self.width * i)) for j in range(self.width)] for i in range(self.height)]
        """
        WHY NOT WORK ? #TODO Check algorithm....
        while not self.__end_of_init(tmp_labyrinth):
            random_choice = random.randint(0,1)
            if random_choice == 0:
                while True:
                    x, y = random.randint(1,self.height-1), random.randint(0,self.width-1)
                    if self.horizontal_wall[x][y]:
                        break
                new_value, old_value = tmp_labyrinth[x][y], tmp_labyrinth[x-1][y]
                if new_value != old_value:
                    self.horizontal_wall[x][y] = False
                    if old_value < new_value:
                        new_value, old_value = old_value, new_value
                    self.__change_value(old_value, new_value, tmp_labyrinth)
            else:
                while True:
                    x, y = random.randint(0,self.height-1), random.randint(1,self.width-1)
                    if self.vertical_wall[x][y]:
                        break
                new_value, old_value = tmp_labyrinth[x][y], tmp_labyrinth[x][y-1]
                if new_value != old_value:
                    self.vertical_wall[x][y] = False
                    if old_value < new_value:
                        new_value, old_value = old_value, new_value
                        self.__change_value(old_value, new_value, tmp_labyrinth)
        """
        while not self.__end_of_init(tmp_labyrinth):
            random_choice = random.randint(0,1)
            if random_choice == 0:
                x, y = random.randint(0,self.height-1), random.randint(1,self.width-1)
                while not self.vertical_wall[x][y]:
                    x, y = random.randint(0,self.height-1), random.randint(1,self.width-1)
                new_value, old_value = tmp_labyrinth[x][y], tmp_labyrinth[x][y-1]
                if new_value != old_value:
                    self.vertical_wall[x][y] = False
                    if old_value < new_value:
                        new_value, old_value = old_value, new_value
                    self.__change_value(old_value, new_value, tmp_labyrinth)
            else:
                x, y = [random.randint(1,self.height-1), random.randint(0,self.width-1)]
                while not self.horizontal_wall[x][y]:
                    x, y = [random.randint(1,self.height-1), random.randint(0,self.width-1)]
                new_value, old_value = tmp_labyrinth[x][y], tmp_labyrinth[x-1][y]
                if new_value != old_value:
                    self.horizontal_wall[x][y] = False
                    if old_value < new_value:
                        new_value, old_value = old_value, new_value
                    self.__change_value(old_value, new_value, tmp_labyrinth)
        self.__create_entry_and_exit()
        self.__write_on_labyrinth()

    def __write_on_labyrinth(self):
        self.labyrinth = \
            [(list(map(lambda x: '1' if x is True else \
                list(map((lambda y: '0' if not y else 'E'),[x]))[0], self.vertical_wall[i//2]))) if i&1 else \
            (list(map(lambda x: '1' if x is True else \
                list(map((lambda y: '0' if not y else 'E'),[x]))[0], self.horizontal_wall[i//2]))) for i in range((self.height*2)+1)]

    
    def write_on_file(self, filename):
        _file = open("rand_lab.txt", 'w')
        for i in range((self.height*2)+1):
            if i&1:
                _file.write("".join(map(lambda x: '1' if x is True else \
                                        list(map((lambda y: '0' if not y else 'E'),[x]))[0], self.vertical_wall[i//2])) + "\n")
            else:
                _file.write("".join(map(lambda x: '1' if x is True else \
                                        list(map((lambda y: '0' if not y else 'E'),[x]))[0], self.horizontal_wall[i//2])) + "\n")

    def __create_entry_and_exit(self):
        for i in range(2):
            if i&1:
                while True:
                    x = random.randrange(1, len(self.vertical_wall)-2, 2)
                    y = random.choice([0, len(self.vertical_wall[x])-1])
                    if self.vertical_wall[x][y]:
                        break
                self.vertical_wall[x][y] = False
                if (not self.entry_position and (random.randint(0,1)==1 or i == 1)):
                    self.vertical_wall[x][y] = 'E'
                    self.entry_position = (x,y)
                else:
                    self.exit_position = (x,y)
            else:
                while True:
                    x = random.choice([0, len(self.horizontal_wall)-1])
                    y = random.randint(1, len(self.horizontal_wall[x])-2)
                    if self.horizontal_wall[x][y]:
                        break
                self.horizontal_wall[x][y] = False
                if (not self.exit_position and (random.randint(0,1)==1 or i == 1)):
                    self.horizontal_wall[x][y] = 'E'
                    self.entry_position = (x,y)
                else:
                    self.exit_position = (x,y)

    def __change_value(self, old_value, new_value, tmp_labyrinth):
        for i in range(self.height):
            for j in range(self.width):
                if tmp_labyrinth[i][j] == old_value:
                    tmp_labyrinth[i][j] = new_value

    def __end_of_init(self, tmp_labyrinth):
        for i in range(self.height):
            for j in range(self.width):
                if tmp_labyrinth[i][j] != 0:
                    return False
        return True


class open_labyrinth(labyrinth):
    """
    Class fille ... OPEN
    """

    def __init__(self, filename):
        self.labyrinth = []
        self.entry_position = None
        self.exit_position = None
        if not self.__create_labyrinth(filename):
            print("Could not create labyrinth")
            exit(1)
        labyrinth.__init__(self, len(self.labyrinth[0]), len(self.labyrinth))

    def __create_labyrinth(self, filename):
        try:
            _file = open(filename, 'r')
        except IOError:
            return False
        read = _file.read().split('\n')

        if read[-1] == '':
            del read[-1]

        height = len(read)-1
        for i, line in enumerate(read):
            self.labyrinth.append([])
            for j, char in enumerate(line):
                self.labyrinth[i].append(char)
                if char == '0' and ((i == 0 or i == height) or (i&1 and (j == 0 or j == len(line)-1))):
                    if self.exit_position:
                        print("Exit already exist...")
                        return False
                    self.exit_position = (i, j)
                if char == 'E':
                    if self.entry_position:
                        print("Entry already exist...")
                        return False
                    self.entry_position = (i, j)
        _file.close()
        if not self.entry_position or not self.exit_position:
            print("No entry or no exit position...")
            return False
        return True

if __name__ == "__main__":
    b = open_labyrinth("test.txt")
    print(b.labyrinth)
