from tkinter import *

window = Tk()

photo = PhotoImage(file= "gif/dog.gif")
label = Label(window, image= photo)

label.pack()

window.mainloop()