from tkinter import *

class GameScreen(Canvas) :
    def __init__(self, mainFrame) :
        Canvas.__init__(self, mainFrame, bg="ivory", width=800, height=450)

    def noGame(self) :
        """Configure l'affichage lorsque aucun labyrinthe n'est lancé"""
        ###METTRE UNE IMAGE "DUNGEON AND PYTHON"
        coord = 1, 1, 800, 450, 1, 450, 800, 1, 1, 1
        self.create_line(coord, fill="red")

    def topView(self) :
        """Configure l'affichage en mode vue du dessus"""
        pass

    def fpsView(self) :
        """Configure l'affichage en mode FPS"""
        pass
