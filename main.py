from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24, "normal"))
my_label.pack()

my_label["text"] = "New text"


def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()


window.mainloop()
