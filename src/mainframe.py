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

        #L'objet jeu
        self.game = None
        
        #Zone d'Affichage
        self.gamescreen = GameScreen(self)
        self.gamescreen.no_game()
        self.gamescreen.pack()

        #Zone de Controle
        self.inputArea = InputArea(self)
        self.inputArea.pack()
        self.inputArea.display_no_game()


        #Raccourcis clavier
        self.bind('<Control-o>', self.menubar.ouvrirFichier)
        self.bind('<Control-g>', self.menubar.genererLabyrinthe)
        self.bind('<Up>', self.inputArea.up)
        self.bind('<Down>', self.inputArea.down)
        self.bind('<Left>', self.inputArea.left)
        self.bind('<Right>', self.inputArea.right)
        
    def no_game() :
        pass

    def open_file(self) :
        filename = filedialog.askopenfilename(parent=None,initialdir="../",title='Veuillez choisir un fichier labyrinthe', filetypes = [('Fichier Labyrinthe', '.lab')])
        #On associe le jeu à la fenetre
        self.game = game.game(False, filename=filename)
        self.init_top_view()

    def generate_labyrinth(self) :
        #On associe le jeu à la fenetre
        self.game = game.game(True, width=20, height=10)
        self.init_top_view()

    def init_top_view(self) :
        self.game.display() #A ENLEVER UNE FOIS QUE L'AFFICHAGE SERA NIQUEL
        #On passe la zone de controle en mode vue du dessus
        self.inputArea.display_top_view()
        #On passe l'ecran de jeu en mode jeu en vue du dessus
        self.gamescreen.init_top_view()
        self.gamescreen.draw()

    def init_fps_view() :
        pass

    #Les méthodes de controle du jeu jeu
    def move(self, direction, *arg) :
        self.game.move(direction)
        self.gamescreen.draw()
