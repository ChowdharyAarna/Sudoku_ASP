from tkinter import *

window = Tk()

buttons = Frame()

mainLabel = Label(text = "Sudoku")

b1 = Button(
    master = buttons,
    text = "1",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b2 = Button(
    master = buttons,
    text = "2",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b3 = Button(
    master = buttons,
    text = "3",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b4 = Button(
    master = buttons,
    text = "4",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b5 = Button(
    master = buttons,
    text = "5",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b6 = Button(
    master = buttons,
    text = "6",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b7 = Button(
    master = buttons,
    text = "7",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b8 = Button(
    master = buttons,
    text = "8",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)

b9 = Button(
    master = buttons,
    text = "9",
    bg = "purple",
    fg = "white",
    width = 5, 
    height = 2
)
mainLabel.pack()

b1.pack(side = "top")
b2.pack(side = "top")
b3.pack(side = "top")
b4.pack(side = "top")
b5.pack(side = "top")
b6.pack(side = "top")
b7.pack(side = "top")
b8.pack(side = "top")
b9.pack(side = "top")

buttons.pack(side = "right")

window.mainloop()