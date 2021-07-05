from tkinter import*

cat = Tk()

#Button without any funtion
Button = Button(cat, text = "Click Me")
Button.pack()

#State disabled button
Button1 = Button(cat, text = "Click", state = DISABLED)
Button1.pack()


mainloop()