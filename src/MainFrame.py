from tkinter import *
from MenuBar import *
from InputArea import *
from GameScreen import *

class MainFrame(Tk) :
    def __init__(self) :
        Tk.__init__(self)

        #MenuBar
        menuBar = MenuBar(self)
        menuBar.pack()

        #Zone d'Affichage
        #LE CANEVAS D'AFFICHAGE SERA UNE CLASSE
        frame = Frame(self)
        canevas = GameScreen(frame)
        frame.pack()

        #Zone de Controle
        inputArea = InputArea(self)
        inputArea.pack()
        
        self.mainloop()
