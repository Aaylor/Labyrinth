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
        self.bind('<Up>', self.move_up)
        self.bind('<Down>', self.move_down)
        self.bind('<Left>', self.move_left)
        self.bind('<Right>', self.move_right)
        
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

    #Les méthodes de controle du jeu
    def move(self, direction, *arg) :
        self.game.move(direction)
        self.gamescreen.draw()
    def move_up(self, *arg) :
        self.move("h")
    def move_down(self, *arg) :
        self.move("b")
    def move_left(self, *arg) :
        self.move("g")
    def move_right(self, *arg) :
        self.move("d")
