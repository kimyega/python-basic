from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")

chk = IntVar()
ch1 = Checkbutton(window, text= "클릭하세요.", variable= chk,
                  command= myFunc)

ch1.pack()

window.mainloop()