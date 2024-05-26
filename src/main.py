from tkinter import *

count = 0

def click():
    print('you clicked a button')
    global count
    count+=1
    print(count)

def submit():
    username= entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)
    
 
def backspaceFun():
     entry.delete(len(entry.get()-1),END) 
    
def DeleteFun():
    entry.delete(0,END) 
    
window = Tk()

# icon =PhotoImage(file='logo.png')
window.geometry('500x500')
window.title("teju demo123")
# window.iconphoto(True,icon)
window.config(background='green')

label = Label(window,text='hey',font=('Arial',14,'bold'),bg='white',
              fg='pink',relief=RAISED,bd=10,padx=20,pady=20,
              )
# label = Label(window,text='hey',font=('Arial',14,'bold'),bg='white',
#               fg='pink',relief=RAISED,bd=10,padx=20,pady=20,image=icon,compound='bottom'
#               )
label.pack()
# label.place(x=20,y=40)

click_button = Button(window,text='click me',command=click,font=('comic sans',14,'bold'),bg='black',
              fg='pink',activebackground='black',activeforeground='pink',state=ACTIVE)
# click_button = Button(window,text='click me',command=click,font=('comic sans',14,'bold'),bg='black',
#               fg='pink',activebackground='black',activeforeground='pink',state=DISABLED,image=icon,compound='bottom')
click_button.pack()

entry = Entry(window,font=('Arial',20),fg='orange',bg='#B942EB')
entry.pack(side=LEFT)

# entry.config(show='*')
# entry.insert(0,'Dummy')
# entry.config(state=DISABLED)

submit_button = Button(window,text='submit',command=submit,font=('comic sans',14,'bold'),bg='black',
              fg='pink',activebackground='black',activeforeground='pink',state=ACTIVE)
submit_button.pack(side=RIGHT)

backspace_button = Button(window,text='backspace',command=backspaceFun,font=('comic sans',14,'bold'),bg='black',
              fg='pink',activebackground='black',activeforeground='pink',state=ACTIVE)
backspace_button.pack(side=RIGHT)

delete_button = Button(window,text='Delete',command=DeleteFun,font=('comic sans',14,'bold'),bg='black',
              fg='pink',activebackground='black',activeforeground='pink',state=ACTIVE)
delete_button.pack(side=RIGHT)

window.mainloop()



def main():
    print("Hello, project is running!")

if __name__ == "__main__":
    main()
