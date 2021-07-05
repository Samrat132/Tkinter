from tkinter import*

dam = Tk()

#creating a lable widget
Label1 = Label(dam, text="Tkinter Program Beginning")
Label2 = Label(dam, text="I am Samrat Rijal")
Label3 = Label(dam, text="Have a good good             ")

#Shoving it onto the screen based upon x-axis and y-axis
#that does not move having a constant position
Label1.grid(row=0, column=0)
Label2.grid(row=1, column=5)
Label3.grid(row=1, column=1)


mainloop()

