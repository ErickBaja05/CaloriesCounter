from tkinter import *

class Program():
    def __init__(self,resizable,width,height,title):
        self.window = Tk()
        if resizable:
            self.window.resizable(1,1)
        else:
            self.window.resizable(0,0)
        self.window.minsize(width,height)
        self.window.title(title)
        
    def modify_window(self,resizable,width,height,title):
        if resizable:
            self.window.resizable(1,1)
        else:
            self.window.resizable(0,0)
        self.window.minsize(width,height)
        self.window.title(title)
    def run_window(self):
        self.window.mainloop()



