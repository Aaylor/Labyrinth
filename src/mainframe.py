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
        self.inputArea.display_no_game()
        
    def no_game() :
        pass

    def top_view(self, game) :
        #On associe le jeu à la fenetre
        self.game = game
        self.game.display() #A ENLEVER UNE FOIS QUE L'AFFICHAGE SERA NIQUEL
        #On passe la zone de controle en mode vue du dessus
        self.inputArea.display_top_view()
        #On passe l'ecran de jeu en mode jeu en vue du dessus
        self.gamescreen.top_view(self.game)
        

    def fps_view() :
        pass
