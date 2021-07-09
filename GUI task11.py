from tkinter import*

root = Tk()

e1 =Entry(root, width=50, fg="blue", bg="white",borderwidth=5)
e1.pack()

def Click():
    textoutput = "Hello"+ e1.get()
    
    Label=Label(root,text=textoutput)

    Label.pack()

Button =Button(root,text="Click Me!", command=Click)
Button.pack()

mainloop()