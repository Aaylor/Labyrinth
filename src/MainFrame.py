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
        self.canevas = GameScreen(self)
        self.canevas.pack(pady=5)

        #Zone de Controle
        inputArea = InputArea(self)
        inputArea.pack()
        
        self.mainloop()
