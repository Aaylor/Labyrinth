from tkinter import *

class GameScreen(Canvas) :
    def __init__(self, mainFrame) :
        Canvas.__init__(mainFrame, bg="ivory", width=800, height=450)
