from tkinter import*

window = Tk()

name = Label (window,text = "Name").grid(row = 0 , column = 0)
e1 = Entry(window).grid(row = 0 , column = 1)

password = Label(window,text = "Password").grid(row = 1 , column = 0)
e2 = Entry(window).grid(row = 1 , column = 1)

submit = Button(window , text = "Submit", state = DISABLED).grid(row = 3, column =1)

mainloop()