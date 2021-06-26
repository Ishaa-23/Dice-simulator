from tkinter import *
import random

root=Tk()
root.title("Dice")
root.geometry("500x400")


label=Label(root,font=('Helvetica',250,'bold'),text='')
label.pack()

def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button=Button(root,font=('helvetics',25,'bold'),text='Roll Dice',command=rolldice,bg='pink')
button.pack()

root.mainloop()