from tkinter import *

FONT = ("Arial", 10, "normal")


def calculate_kms():
    miles = float(miles_input.get())
    km = miles * 1.609
    conversion_label.config(text=f"{round(km, 1)}")


window = Tk()
window.title("Miles to MK Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=5, pady=5)

conversion_label = Label(text=0, font=FONT)
conversion_label.grid(column=1, row=1)
conversion_label.config(padx=5, pady=5)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate_kms)
button.grid(column=1, row=2)


window.mainloop()
