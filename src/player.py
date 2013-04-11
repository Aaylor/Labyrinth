class Player(object):
    """Classe qui contiendra les informations sur le joueur (position, direction,  
    eventuellement des trucs qui viendront plus tard(bonus, nombre de vie etc.)
    On utilise une classe pour parrer à l'eventuallité d'un mode VS"""
    
    def __init__(self, position, lab_size):
        self.position = position
        self.__set_first_direction(lab_size)

    def __set_first_direction(self, lab_size):
        x, y = self.position
        if (x == 0):
            self.direction = 'b'
        elif (y == 0):
            self.direction = 'd'
        elif (x == lab_size[0]):
            self.direction = 'h'
        else:
            self.direction = 'g'
