from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "normal"))
my_label["text"] = "New text"
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Button2
button2 = Button(text="New Button", command=button_clicked)
# button2.pack()
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
