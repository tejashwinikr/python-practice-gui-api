from tkinter import *

count = 0
food = ['pizza', 'hamburger', 'salad']

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

def create_window():
    global entry, x, f, tempscale
    
    window = Tk()
    window.geometry('700x500')
    window.title("Teju Demo")
    window.config(background='green')

    label = Label(window, text='Hey', font=('Arial', 14, 'bold'), bg='white', fg='pink', relief=RAISED, bd=10, padx=20, pady=20)
    label.pack(pady=10)

    click_button = Button(window, text='Click Me', command=click, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    click_button.pack(pady=10)

    entry = Entry(window, font=('Arial', 20), fg='orange', bg='#B942EB')
    entry.pack(pady=10,side=LEFT)

    submit_button = Button(window, text='Submit', command=submit, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    submit_button.pack(side=RIGHT, padx=5)

    backspace_button = Button(window, text='Backspace', command=backspaceFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    backspace_button.pack(side=RIGHT, padx=5)

    delete_button = Button(window, text='Delete', command=DeleteFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    delete_button.pack(side=RIGHT, padx=5)

    x = IntVar()
    checkbox = Checkbutton(window, text='I agree to this', variable=x, onvalue=1, offvalue=0, command=checkFun, font=('Arial', 20), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    checkbox.pack(pady=10)

    f = IntVar()
    for index, food_item in enumerate(food):
        radio = Radiobutton(window, text=food_item, variable=f, value=index, padx=25, font=('Impact', 20), command=order)
        radio.pack(anchor=W)

    tempscale = Scale(window, from_=100, to=0, length=300, orient=VERTICAL, font=('Consolas', 20), tickinterval=10, showvalue=0, resolution=5, fg='#FF1C00', bg='#36E0F1')
    tempscale.pack(side=LEFT, padx=20, pady=20)

    tempscale_button = Button(window, text='Temp Submit', command=tempscaleFun, font=('Comic Sans', 14, 'bold'), bg='black', fg='pink', activebackground='black', activeforeground='pink')
    tempscale_button.pack(side=LEFT, padx=20, pady=20)

    window.mainloop()
