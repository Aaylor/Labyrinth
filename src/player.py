class Player(object):
    """Classe qui contiendra les informations sur le joueur (position, direction,  
    eventuellement des trucs qui viendront plus tard(bonus, nombre de vie etc.)
    On utilise une classe pour parrer à l'eventuallité d'un mode VS"""
    def __init__(self, position, direction, loaded_gif):
        self.position, self.direction, self.loaded_gif = (position, direction,
                                                          loaded_gif)
