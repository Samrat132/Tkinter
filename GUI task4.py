from tkinter import*

window = Tk()
window.geometry("800x500")

name = Label (window, text = "Name").place( x=30 , y=50)
address = Label (window, text = "Address").place( x=30 , y=90)
contact = Label (window, text = "Contact").place( x=30 , y=130)

e1 = Entry(window).place(x=80 , y=50)
e2 = Entry(window).place(x=80 , y=90)
e3 = Entry(window).place(x=80 , y=130)

submit = Button(window,text = "Submit").place (x=100, y=150)


mainloop()