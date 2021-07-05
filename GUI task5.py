from tinkter import*

dam = Tk()

#creating a lable widget
Label1 = Label(dam, text="Tkinter Program Beginning")
Lable2 = Lable(dam, text="I am Samrat Rijal")
Lable3 = Lable(dam, text="Have a good good")

#Shoving it onto the screen based upon x-axis and y-axis
#that does not move having a constant position
Lable1.grid(row=0, column=0)
Lable2.grid(row=1, column=5)
Lable3.grid(row=1, column=1)


mainloop()

