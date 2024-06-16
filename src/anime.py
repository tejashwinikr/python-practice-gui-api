from tkinter import *
import time
import os

WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1

def anime_window():
    window2 = Tk()
    
    canvas = Canvas(window2,width=WIDTH,height=HEIGHT)
    canvas.pack()
    
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # icon_path = os.path.join(base_path, 'png-icons', 'star.png')
    # print(os.path.join(base_path, 'png-icons', 'star.png'))
    space_path = os.path.join(base_path,'png-icons','star.png')
    # photo_image = PhotoImage(file=space_path)
    
    # my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)
    
    
    background_photo = PhotoImage(file=space_path)
    background = canvas.create_image(0,0,image=background_photo,anchor=NW)

    photo_image =  PhotoImage(file=space_path)
    my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

    image_width = photo_image.width()
    image_height = photo_image.height()

    while True:
        coordinates = canvas.coords(my_image)
        print(coordinates)
        if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
            xVelocity = -xVelocity
        if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
            yVelocity = -yVelocity
        canvas.move(my_image,xVelocity,yVelocity)
        window2.update()
        time.sleep(0.01)
    
    window2.mainloop()