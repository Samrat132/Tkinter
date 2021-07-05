from tkinter import*

int = Tk()

def Click():
    myLabel = Label(int, text = "Button is clicked!!")
    myLabel.pack()


Button = Button(int, text = "Click Me!", command=Click)
Button.pack()

mainloop()