from tkinter import *
from menubar import *
from input_area import *
from gamescreen import *

class MainFrame(Tk) :
    def __init__(self) :
        Tk.__init__(self)

        #MenuBar
        self.menubar = MenuBar(self)
        self.menubar.pack()

        #Zone d'Affichage
        self.gamescreen = GameScreen(self)
        self.gamescreen.no_game()
        self.gamescreen.pack()

        #Zone de Controle
        self.inputArea = InputArea(self)
        self.inputArea.pack()
        
    def no_game() :
        pass

    def top_view(self, game) :
        self.game = game
        self.game.display()
        self.gamescreen.top_view(self.game)
        

    def fps_view() :
        pass
