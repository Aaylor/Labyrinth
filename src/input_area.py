from tkinter import *

class InputArea(Frame) :
    def __init__(self, mainFrame) :
        Frame.__init__(self, mainFrame)
        self.no_game_controls = self.no_game_controls()
        self.top_view_controls = self.top_view_controls()
        self.fps_view_controls = self.fps_view_controls()

    def no_game_controls(self) :
        frame = Frame(self)
        
        #Bouton Generer Labyrinthe
        genererButton = Button(frame, text="Générer un Labyrinthe")
        genererButton.pack(side=LEFT)

        #Bouton Ouvrir Labyrinthe
        ouvrirButton = Button(frame, text="Ouvrir un Labyrinthe")
        ouvrirButton.pack(side=RIGHT)

        return frame

    def top_view_controls(self) :
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

    def fps_view_controls(self) :
        pass
