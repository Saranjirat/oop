from tkinter import ttk
from tkinter import *

root = Tk()
root.option_add("*Font","impact 18")
root.title("kuy")
photo = [PhotoImage(file='PLANTATION.png'),PhotoImage(file='HORIZON.png')]
j=1
for i in photo:
    Label(root, image=i, borderwidth=0 ).pack(ipadx = 100+j)
    j+=100

root.mainloop()
