from tkinter import*

window  = Tk()

sambutton = Button(window, text ="LEFT" , fg = "green")
sambutton.pack(side = LEFT)

sambutton = Button(window, text = "RIGHT" , fg ="red")
sambutton.pack(side = RIGHT)

sambutton = Button(window, text ="TOP" , fg = "black")
sambutton.pack(side = TOP)

sambutton = Button(window, text ="BOTTOM" , fg = "blue")
sambutton.pack(side = BOTTOM)

mainloop()