from tkinter import *

class InputArea(Frame) :
    def __init__(self, mainFrame) :
        Frame.__init__(self, mainFrame)
        #Bon Changer de Vue
        displayFrame = Frame(self)
        displayFrame.pack(side=BOTTOM)
        displayButton = Button(displayFrame, text="Changer de vue")
        displayButton.pack(side=RIGHT)

        
        directionFrame = Frame(self, pady = 5)
        directionFrame.pack(side=BOTTOM)
        #Bouton Haut
        upFrame = Frame(directionFrame)
        upFrame.pack(side=TOP)
        upButton = Button(upFrame, text="Haut", width=7)
        upButton.pack()

        #Bouton Gauche, Bas, Droite
        bottomFrame = Frame(directionFrame)
        bottomFrame.pack(side=BOTTOM)
        leftButton = Button(bottomFrame, text="Gauche", width=7)
        leftButton.pack(side=LEFT) 
        downButton = Button(bottomFrame, text="Bas", width=7)
        downButton.pack(side=LEFT)
        rightButton = Button(bottomFrame, text="Droit", width=7)
        rightButton.pack(side=LEFT)
