from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=150)
frm.grid()
ttk.Label(frm, text="Calculator").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="+", command=root.destroy).grid(column=2, row=0)
ttk.Button(frm, text="-", command=root.destroy).grid(column=2, row=1)
ttk.Button(frm, text="*", command=root.destroy).grid(column=2, row=2)
ttk.Button(frm, text="/", command=root.destroy).grid(column=2, row=3)
root.mainloop()