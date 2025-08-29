from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def myFunc() :
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")

window = Tk()

img = Image.open("C:/pycham/dog.jpg")
img = img.resize((150, 150))
photo = ImageTk.PhotoImage(img)


button1 = Button(window, image= photo, command= myFunc)
button1.pack()

window.mainloop()

