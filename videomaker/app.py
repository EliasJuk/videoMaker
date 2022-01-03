from tkinter import *

class Gui():
  def __init__(self):
    self.root = Tk()
    self.window()
    self.root.mainloop()


  def window(self):    
    self.root.geometry("600x400")


if __name__ == '__main__':
  app = Gui()