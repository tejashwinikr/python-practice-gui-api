from tkinter import *

count = 0

def click():
    print('you clicked a button')
    global count
    count+=1
    print(count)
    
    
window = Tk()

# icon =PhotoImage(file='logo.png')
window.geometry('420x420')
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

window.mainloop()



# def main():
#     print("Hello, world!")

# if __name__ == "__main__":
#     main()
