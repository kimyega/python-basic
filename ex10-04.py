from tkinter import *
from PIL import Image, ImageTk


window = Tk()

img = Image.open("C:/pycham/dog.jpg")
photo = ImageTk.PhotoImage(img)


label1 = Label(window, image= photo)
label1.pack()

window.mainloop()