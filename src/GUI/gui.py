from tkinter import *
from tkinter import messagebox,colorchooser,filedialog #submodules
# from tkinter.ttk import *
import time
import os

count = 0
food = ['pizza', 'hamburger', 'salad']
window = Tk()
percent = StringVar()
text= StringVar()
icon_path = os.path.join(os.path.dirname(__file__), 'star.png')
myimage = PhotoImage(file=icon_path)

def click():
    global count
    count += 1
    print(f'Button clicked {count} times')

def submit():
    username = entry.get()
    print(f"Hello {username}")
    entry.config(state=DISABLED)

def backspaceFun():
    entry.delete(len(entry.get()) - 1, END)

def DeleteFun():
    entry.delete(0, END)

def checkFun():
    if x.get() == 1:
        print("You agreed to this")
    else:
        print("You don't agree!!")

def order():
    print(f"You ordered {food[f.get()]}")

def tempscaleFun():
    print(f"The temperature is {tempscale.get()}° Celsius")
    
def listboxFun():
    # print("You have ordered") #singleitem
    # print(listbox.get(listbox.curselection()))
    food =[]
    #MULTIPLE MODE
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
        
    print("You have ordered")
    for index in food:
         print(index)

def addToList():
    listbox.insert(listbox.size(),entryToList.get())
    entryToList.delete(0,END)
    listbox.config(height=listbox.size())

def deleteFromList():
    #single selection
    # listbox.delete(listbox.curselection())
    # listbox.config(height=listbox.size())
    
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
        
    listbox.config(height=listbox.size())
    
def messageFun():
    # messagebox.showinfo(title='This is an info message box',message='oh hi there buddy')
    # messagebox.showwarning(title='Warning',message='be careful') 
    # messagebox.showerror(title='ERROR', message='Something went wrong')
      
    #returns boolean value  
    # if messagebox.askokcancel(title='ask ok cancel',message='do you wanna have ramyoen'):
    #     print("lets go!!!!")
    # else:
    #     print('do u wanna see my cat')    
    
    # if messagebox.askretrycancel(title='ask ok cancel',message='do you wanna try one more time'):
    #     print("one more round!!!!")
    # else:
    #     print('lets try one more time')  
       
    # if messagebox.askyesno(title='ask yes no',message='do you wanna try one more time'):
    #     print("one more round!!!!")
    # else:
    #     print('lets try one more time')   
    
    #returns yes or no string
    #print(messagebox.askquestion(title='ask question',message='do you like me'))
    # answer =messagebox.askquestion(title='ask question',message='do you like me')
    # if(answer == 'yes'): print('hey good taste')
    # else: print(' nevermind')
    
    #returns True,False,None string
    print(messagebox.askyesnocancel(title='yes/no/cancel',message='do u wanna come over?',icon='error'))
  
def colorFun():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)#change backgorund color
    
def textAreaFun():
    input = textArea.get('1.0',END)
    print(input)

def openFile():
    filePath = filedialog.askopenfilename(title='open file okay?',
                                          filetypes=(('text files','.txt'),("all files",".*")) )
    print(filePath)  
    file=open(filePath,'r')
    print(file.read())
    file.close()
    #filePath = filedialog.askopenfilename(initialdir="c:\\user")

def saveFile():
    file= filedialog.asksaveasfile(defaultextension='.txt',
                                   filetypes=[
                                       ('Text file','.txt'),
                                       ('Html file','.html'),
                                       ('All file','.*'),
                                   ]
                                   #initialdir=''
                                   )
    if file is None:
        return
    filetext=str(suga_text.get(1.0,END))
    #filetext = input('enter some text i guess) #through console getting data
    file.write(filetext)
    file.close()
  
def editCutFun():
    print("you copied some text!")
    
def editCopyFun():
     print("you copied some text!")
   
def editPasteFun():
    print("you pastied some text!")

def create_subwindow():
    new_window = Tk() # Toplevel()= new window 'on top' of other winows,linked to a 'bottom'window
                      #Tk()= new independent window
    window.destroy()#close out of old window
   
def submit_grid():
    print(' hey there babe')
    
def start():
    tasks =10
    x=0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set(str(int((x/tasks)*100))+"%")
        text.set(str(x) + "/" + str(tasks)+ " tasks completed")
        window.update_idletasks()
       
def doSomethingOnKEY(event):
    # print("You pressed: " + event.keysym)
    key_ev_label.config(text=event.keysym)

def doSomethingOnMouse(event):
    print("You did something on mouse!!" + str(event.x) +" "+ str(event.y))
   
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)   
   
def move_up(event):
    label_imageMove.place(x= label_imageMove.winfo_x(), y= label_imageMove.winfo_y()-10)
def move_down(event):
    label_imageMove.place(x= label_imageMove.winfo_x(), y= label_imageMove.winfo_y()+10)
def move_left(event):
    label_imageMove.place(x= label_imageMove.winfo_x()-10, y= label_imageMove.winfo_y())
def move_right(event):
    label_imageMove.place(x= label_imageMove.winfo_x()+10, y=label_imageMove.winfo_y())
   
def move_up_canvas(event):
   canvas.move(canvaImage,0,-10)
def move_down_canvas(event):
   canvas.move(canvaImage,0,10)
def move_left_canvas(event):
   canvas.move(canvaImage,-10,0)
def move_right_canvas(event):
   canvas.move(canvaImage,10,0)
   
#main gui function 
def create_window():
    global entry, x, f, tempscale,listbox,entryToList,delete_item_button,msg_btn,jin_button
    global textArea,file_btn,suga_text,bar, key_ev_label, label_imageMove,canvas,canvaImage
    
   
    window.geometry('700x500')
    window.title("Teju Demo")
    # window.config(background='green')
    
      # Load the image
    # icon_path = os.path.join(os.path.dirname(__file__), '..', 'png-icons', 'star.png')
    # icon = PhotoImage(file=icon_path)
    # window.iconphoto(True,icon)

    # #label = Label(window, text='Hey', font=('Arial', 14, 'bold'), bg='white', fg='pink', relief=RAISED, bd=10, padx=20, pady=20)
    #  # label.pack(pady=10)

    # click_button = Button(window, text='Click Me', command=click, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    #  # click_button.pack(pady=10)

    # entry = Entry(window, font=('Arial', 20), fg='orange', bg='#B942EB')
    #  # entry.pack(pady=10,side=LEFT)

    # submit_button = Button(window, text='Submit', command=submit, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    #  # submit_button.pack(side=RIGHT, padx=5)

    # backspace_button = Button(window, text='Backspace', command=backspaceFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    #  # backspace_button.pack(side=RIGHT, padx=5)

    # delete_button = Button(window, text='Delete', command=DeleteFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    #  # delete_button.pack(side=RIGHT, padx=5)

    # x = IntVar()
    # checkbox = Checkbutton(window, text='I agree to this', variable=x, onvalue=1, offvalue=0, command=checkFun, font=('Arial', 20), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    #  # checkbox.pack(pady=10)

    # f = IntVar()
    # for index, food_item in enumerate(food):
    #     radio = Radiobutton(window, text=food_item, variable=f, value=index, padx=25, font=('Impact', 20), command=order)
    #     # radio.pack(anchor=W)

    # tempscale = Scale(window, from_=100, to=0, length=300, orient=VERTICAL, font=('Consolas', 20), tickinterval=10, showvalue=0, resolution=5, fg='#FF1C00', bg='#36E0F1')
    # # tempscale.pack(side=LEFT, padx=20, pady=20)

    # tempscale_button = Button(window, text='Temp Submit', command=tempscaleFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    #  # tempscale_button.pack(side=LEFT, padx=20, pady=20)
    
    # #listbox feature
    # listbox = Listbox(window,
    #                   bg='#f7ffde',
    #                   font=("Constantia",35),
    #                   width=32,
    #                   selectmode=MULTIPLE)
    # # listbox.pack()
    
    # listbox.insert(1,'pizza')
    # listbox.insert(2,'pasta')
    # listbox.insert(3,'noodles')
    # listbox.insert(4,'soup')
    # listbox.insert(5,'salad')
    
    # listbox.config(height=listbox.size())
    
    # entryToList = Entry(window, font=('Arial', 20), fg='orange', bg='#B942EB')
    # # entryToList.pack(pady=10,side=LEFT)
    
    # listbox_submit_button = Button(window, text='Submit order', command=listboxFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    # # listbox_submit_button.pack(side=RIGHT, padx=5)
    
    # add_button = Button(window, text='Add item', command=addToList, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    # # add_button.pack(side=RIGHT, padx=5)
    
    # delete_item_button = Button(window, text='delete item', command=deleteFromList, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    # # delete_item_button.pack(side=RIGHT, padx=5)

    # #message window
    # msg_btn =Button(window,command=messageFun,text='Click me')
    # # msg_btn.pack()
    
    # #colorchooser submodule
    # jin_button = Button(window,command=colorFun,text='click me')
    # #jin_button.pack()
    
    # #text widget,multiple lines
    # textArea = Text(window,
    #                 bg='light yellow',
    #                 font=('Ink Free',13),
    #                 height=5,
    #                 width=20,
    #                 padx=20,
    #                 pady=20,
    #                 border='1px solid pink',
    #                 fg='purple')
    # # textArea.pack()
        
    # text_submit_button = Button(window, text='submit summary', command=textAreaFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    # #text_submit_button.pack(side=RIGHT, padx=5)
    
    # #filedialog,file opne
    # file_btn = Button(window,command=openFile,text='choose a file')
    # # file_btn.pack()
    
    # #save a file
    # suga_btn = Button(window,command=saveFile,text='save file')
    # # suga_btn.pack()
    
    # suga_text= Text(window)
    # # suga_text.pack()
    
    # #menu options
    # menubar = Menu(window)
    # # window.config(menu=menubar)
    
    # openImage = PhotoImage(file='')
    # saveImage = PhotoImage(file='')
    # exitImage = PhotoImage(file='')
    
    # fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
    # menubar.add_cascade(label="File",menu=fileMenu)
    # fileMenu.add_command(label='Open',command=openFile)
    # # fileMenu.add_command(label='Open',command=openFile,image=openImage,compound='left)
    # fileMenu.add_command(label='Save',command=saveFile)
    # fileMenu.add_separator()
    # fileMenu.add_command(label='Exit',command=quit)
    
    # editMenu =Menu(menubar,tearoff=0,font=("MV Boli",15))
    # menubar.add_cascade(label='Edit',menu=editMenu)
    # editMenu.add_command(label='Cut',command=editCutFun)
    # editMenu.add_command(label='Copy',command=editCopyFun)
    # editMenu.add_command(label='Paste',command=editPasteFun)
    
    #frame = a rectangular container to group and hold widgets
    # frame = Frame(window,bg='pink',bd=10,relief=SUNKEN)
    #bd=10,relief=RAISED , SUNKEN ,frame.pack(),frame.pack(x=0,y=0)
    # frame.pack(side=BOTTOM)
    # Button(frame,text='S',font=("Consolas",25),width=3).pack(side=TOP)
    # Button(frame,text='u',font=("Consolas",25),width=3).pack(side=LEFT)
    # Button(frame,text='g',font=("Consolas",25),width=3).pack(side=LEFT)
    # Button(frame,text='a',font=("Consolas",25),width=3).pack(side=LEFT)
    
    #new window
    #Button(window,text='create new window',command=create_subwindow).pack()
    
    #tabs ttk notebook is from
    #notebook = Notebook(window) # widgets that manages a collection of windowa/displays
    
    # tab1 = Frame(notebook) #new frame for tab1
    # tab2 = Frame(notebook) #new frame for tab2
    
    # notebook.add(tab1,text='Tab 1')
    # notebook.add(tab2,text='Tab 2')
    #notebook.pack(expand=True) # expand = expand to fill any space not otherwise used
    
    # Label(tab1,text='Hellow,this is tab1',width=50,height=25).pack()
    # Label(tab2,text='alhoa,this is tab2',width=50,height=25).pack()
    
    #grid -geometry manager that oraganizes widgets in a table-like structure in a parent
    # titleLabel = Label(window,text='Enter your info',font=("Arial",25)).grid(row=0,column=0)
    # firstNameLabel = Label(window,text='First name:',bg='red',width=20).grid(row=1,column=0)
    # firstNameEntry = Entry(window).grid(row=1,column=1)
    
    # lasttNameLabel = Label(window,text='Last name :',bg='green').grid(row=2,column=0)
    # lastNameEntry = Entry(window).grid(row=2,column=1)

    # emailLabel = Label(window,text='Email :',bg='blue').grid(row=3,column=0)
    # emailEntry = Entry(window).grid(row=3,column=1)
    
    # Button(window,text='Submit',command=submit_grid).grid(row=4,column=0,columnspan=2)
    
    #progressbar ttk
    #bar = Progressbar(window,orient=HORIZONTAL,length=300)
    # bar.pack(pady=10)
    
    # percentLabel = Label(window,textvariable=percent).pack()
       
    # textLabel = Label(window,textvariable=text).pack()
    # bar_button =  Button(window,text='download',command=start).pack()
    
    # canvas =  widget that is used to draw graphs, plots, images in a window
    canvas = Canvas(window,height=400,width=500)
    #canvas.create_line(0,0,500,500,fill="blue",width=5)
    #canvas.create_line(0,500,500,0,fill="red",width=5)
    #canvas.create_rectangle(50,50,250,250,fill="purple")
    points = [250,0,500,500,0,500]
    #canvas.create_polygon(points,fill="yellow",outline="black",width=5)
    #canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)
    #canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
    #canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
    #canvas.create_oval(190,190,310,310,fill="white",width=10)
    #canvas.pack()
    
    #keyboard events
    # window.bind("<Key>",doSomethingOnKEY)

    key_ev_label = Label(window,font=("Helvetica",100))
    # key_ev_label.pack()
    
    #mouse events
    #window.bind("<Button-1>",doSomethingOnMouse)#left mouse click
    #window.bind("<Button-2>",doSomethingOnMouse) #scroll wheel
    #window.bind("<Button-3>",doSomethingOnMouse) #right mouse click
    #window.bind("<ButtonRelease>",doSomethingOnMouse)#mousebutton release
    #window.bind("<Enter>",doSomethingOnMouse) #enter the window
    #window.bind("<Leave>",doSomethingOnMouse) #leave the window
    #window.bind("<Motion>",doSomethingOnMouse) #Where the mouse moved
    
    #drag and drop
    label = Label(window,background='red',width=10,height=5)
    # label.place(x=0,y=0)

    # label2 = Label(window,background="blue",width=10,height=5)
    # label2.place(x=100,y=100)

    # label.bind("<Button-1>",drag_start)
    # label.bind("<B1-Motion>",drag_motion)

    # label2.bind("<Button-1>",drag_start)
    # label2.bind("<B1-Motion>",drag_motion)
    
    #move images on window using keys and updown
    # window.bind("<w>",move_up)
    # window.bind("<s>",move_down)
    # window.bind("<a>",move_left)
    # window.bind("<d>",move_right)
    # window.bind("<Up>",move_up)
    # window.bind("<Down>",move_down)
    # window.bind("<Left>",move_left)
    # window.bind("<Right>",move_right)


    # label_imageMove = Label(window,image=myimage)
    # label_imageMove.place(x=0,y=0)
    
    #move images on canvas
    # window.bind("<w>",move_up_canvas)
    # window.bind("<s>",move_down_canvas)
    # window.bind("<a>",move_left_canvas)
    # window.bind("<d>",move_right_canvas)

    # canvas = Canvas(window,width=1000,height=1000)
    # canvas.pack()

    # canvaImage = canvas.create_image(0,0,image=myimage,anchor=NW)
    
    #2d animations
    
    window.mainloop()
