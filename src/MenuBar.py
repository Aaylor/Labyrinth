from tkinter import *

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
