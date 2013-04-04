from tkinter import *
from menubar import *
from input_area import *
from gamescreen import *

class MainFrame(Tk) :
    def __init__(self) :
        Tk.__init__(self)

        #MenuBar
        self.menuBar = MenuBar(self)
        self.menuBar.pack()

        #Zone d'Affichage
        self.gameScreen = GameScreen(self)
        self.gameScreen.pack()

        #Zone de Controle
        self.inputArea = InputArea(self)
        self.inputArea.pack()
        
