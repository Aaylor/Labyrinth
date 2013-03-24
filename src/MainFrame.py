from tkinter import *


class MainFrame(Tk) :
    def __init__(self) :
        Tk.__init__(self)

        #MenuBar
        menuBar = MenuBar(self)
        menuBar.pack()

        #Zone d'Affichage
        self.canevas = Canvas(self, bg="ivory", width=800, height=450)
        self.canevas.pack(pady=5)

        #Zone de Controle
        inputArea = InputArea(self)
        inputArea.pack()
        
        self.mainloop()

class MenuBar(Frame) :
    def __init__(self, mainFrame) :
        Frame.__init__(self, mainFrame)
        self.menuBar = Menu(self)
        self.master.config(menu=self.menuBar)

        #Menu Fichier
        fichierMenu = Menu(self, tearoff = 0)
        self.menuBar.add_cascade(label="Fichier", menu=fichierMenu)
        fichierMenu.add_command(label="Nouvelle partie")
        fichierMenu.add_command(label="Ouvrir une Partie")
        fichierMenu.add_command(label="Enregistrer Partie")
        fichierMenu.add_separator()
        fichierMenu.add_command(label="Quitter")

        #Menu Aide
        aideMenu=Menu(self, tearoff=0)
        self.menuBar.add_cascade(label="Aide", menu=aideMenu)
        aideMenu.add_command(label="A propos")

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
    
        
        

fenetre = MainFrame()
        
