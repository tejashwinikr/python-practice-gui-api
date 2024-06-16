from tkinter import *
import time
import os

WIDTH = 500
HEIGHT = 500

def anime_window():
    window2 = Tk()
    
    canvas = Canvas(window2,width=WIDTH,height=HEIGHT)
    canvas.pack()
    
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # icon_path = os.path.join(base_path, 'png-icons', 'star.png')
    # print(os.path.join(base_path, 'png-icons', 'star.png'))
    space_path = os.path.join(base_path,'png-icons','space.png')
    photo_image = PhotoImage(file=space_path)
    
    window2.mainloop()