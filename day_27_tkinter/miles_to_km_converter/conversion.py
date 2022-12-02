from tkinter import Tk
from tkinter import ttk
from tkinter import Button
from tkinter import Entry


window = Tk()
window.title("Mile to Km Converter")

window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

miles_label = ttk.Label(text="Miles", font="Arial")
miles_label.grid(column=2, row=0, padx=10, pady=10)

km_label = ttk.Label(text="Km", font="Arial")
km_label.grid(column=2, row=1, padx=10, pady=10)

is_equal_label = ttk.Label(text="is equal to", font="Arial")
is_equal_label.grid(column=0, row=1, padx=10, pady=10)

km_conversion_output_label = ttk.Label(text="0", font="Arial")
km_conversion_output_label.grid(column=1, row=1, padx=10, pady=10)


def calculate_fetch_input():
    miles_input = int(miles_input_box.get())
    conversion_formula = miles_input * 1.609344
    km_conversion_output_label.config(text=conversion_formula)


calculate_button = Button(text="Calculate", width=10, height=1, font=("Arial", 11), command=calculate_fetch_input)
calculate_button.grid(column=1, row=2, padx=10, pady=10)

miles_input_box = Entry(width=10, highlightcolor="blue", font=("Arial", 11), justify="center")
miles_input_box.grid(column=1, row=0)
window.mainloop()
