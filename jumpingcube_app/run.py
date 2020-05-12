from tkinter import *
from tkinter import messagebox

def clicked():

    messagebox.showinfo('Retry', 'Vise srece ovaj put!')


def main():

    global canvas, window
    window = Tk()
    window.title('Jumping_cube')
    window.geometry('500x300')
    window.configure(background="black")

    lbl_name=Label(window,text="Unesite ime:",font=("Romantic",16),bg="bisque2",fg="black")
    lbl_name.pack()
    entry_name=Entry(window)
    entry_name.pack()

    lbl_points = Label(window, text="Poeni:",bg="bisque2",font=("Romantic",16),fg="black",width=10,heigh=3)
    lbl_points.pack(pady=30)

    btn_retry = Button(window, text='Retry', command=clicked)
    btn_retry.pack(pady=30)



   #canvas = Canvas(window, width=100, height=100, background='black')

    window.mainloop()

main()