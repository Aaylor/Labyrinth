from tkinter import *

class GameScreen(Canvas) :
    def __init__(self, mainFrame) :
        Frame.__init__(self, mainFrame)
        
        gameScreen = Canvas(self, bg="ivory", width=800, height=450) 
        gameScreen.pack()
