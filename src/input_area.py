from tkinter import *

class InputArea(Frame) :
    def __init__(self, mainFrame) :
        Frame.__init__(self, mainFrame)
        self.mainFrame = mainFrame
        self.no_game_controls = self.no_game_controls()
        self.top_view_controls = self.top_view_controls()
        self.fps_view_controls = self.fps_view_controls()



    #Methodes de creation des zones de controle
        
    def no_game_controls(self) :
        """Retourne la zone de controle en mode "No Game", proposant de generer un Labyrinthe ou d'en ouvrir un"""
        frame = Frame(self)
        
        #Bouton Generer Labyrinthe
        genererButton = Button(frame, text="Générer un Labyrinthe", command=self.mainFrame.menubar.genererLabyrinthe)
        genererButton.pack(side=LEFT)

        #Bouton Ouvrir Labyrinthe
        ouvrirButton = Button(frame, text="Ouvrir un Labyrinthe", command=self.mainFrame.menubar.ouvrirFichier)
        ouvrirButton.pack(side=RIGHT)

        return frame

    def top_view_controls(self) :
        """Retourne la zone de controle en mode "Vue du dessus" """
        #Construction des Frames
        frame = Frame(self)
        displayFrame = Frame(frame)
        displayFrame.pack(side=BOTTOM)
        directionFrame = Frame(frame, pady = 5)
        directionFrame.pack(side=BOTTOM)
        upFrame = Frame(directionFrame)
        upFrame.pack(side=TOP)
        bottomFrame = Frame(directionFrame)
        bottomFrame.pack(side=BOTTOM)
        
        #Bouton Changer de Vue
        displayButton = Button(displayFrame, text="Changer de vue")
        displayButton.pack(side=RIGHT)
        

        #Bouton Haut
        upButton = Button(upFrame, text="Haut", width=7, command=self.mainFrame.move_up)
        upButton.pack()

        #Bouton Gauche, Bas, Droite
        leftButton = Button(bottomFrame, text="Gauche", width=7, command=self.mainFrame.move_left)
        leftButton.pack(side=LEFT) 
        downButton = Button(bottomFrame, text="Bas", width=7, command=self.mainFrame.move_down)
        downButton.pack(side=LEFT)
        rightButton = Button(bottomFrame, text="Droit", width=7, command=self.mainFrame.move_right)
        rightButton.pack(side=LEFT)

        return frame

    def fps_view_controls(self) :
        """Retourne la zone de controle en mode "Vue a la premiere personne" """
        #Construction des Frames
        frame = Frame(self)
        displayFrame = Frame(frame)
        displayFrame.pack(side=BOTTOM)
        directionFrame = Frame(frame, pady = 5)
        directionFrame.pack(side=BOTTOM)
        upFrame = Frame(directionFrame)
        upFrame.pack(side=TOP)
        bottomFrame = Frame(directionFrame)
        bottomFrame.pack(side=BOTTOM)
        
        #Bouton Changer de Vue
        displayButton = Button(displayFrame, text="Changer de vue")
        displayButton.pack(side=RIGHT)
        

        #Bouton Haut
        upButton = Button(upFrame, text="Haut", width=7)
        upButton.pack()

        #Bouton Gauche, Bas, Droite
        leftButton = Button(bottomFrame, text="Gauche", width=7)
        leftButton.pack(side=LEFT) 
        downButton = Button(bottomFrame, text="Bas", width=7)
        downButton.pack(side=LEFT)
        rightButton = Button(bottomFrame, text="Droit", width=7)
        rightButton.pack(side=LEFT)

        return frame

    #Methode permettant d'afficher et de cacher les zones de controles

    def display_no_game(self) :
        """Affiche les controles du mode "Sans jeu" et cache les autres controles"""
        self.no_game_controls.pack()
        self.top_view_controls.pack_forget()
        self.fps_view_controls.pack_forget()

    def display_top_view(self) :
        """Affiche les controles du mode "Vue du dessus" et cache les autres controles"""
        self.no_game_controls.pack_forget()
        self.top_view_controls.pack()
        self.fps_view_controls.pack_forget()

    def display_fps_view(self) :
        """Affiche les controles du mode "Vue a la premiere personne" et cache les autres controles"""
        self.no_game_controls.pack_forget()
        self.top_view_controls.pack_forget()
        self.fps_view_controls.pack()
