import tkinter
from msilib.schema import RadioButton
from tkinter import ttk
from tkinter import Button
from tkinter import Entry
from tkinter import Text
from tkinter import END
from tkinter import Scale
from tkinter import IntVar
from tkinter import Checkbutton
from tkinter import Radiobutton
from tkinter import Listbox

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
main_label = ttk.Label(text="Conversion", font=("Arial", 24, "bold"))
window.config(padx=20, pady=20)
# main_label.pack(expand=False)

main_label["text"] = "New Text"
main_label.config(text="New Text")
main_label.grid(column=0, row=0, padx=50, pady=50)

def button_clicked():
    main_label.config(text=new_input.get())


def button_2_clicked():
    button2.config(text="Haha, you clicked me!")


new_input = Entry(width=50)
new_input.insert(END, string="Some text to begin with.")
print(new_input.get())
new_input.grid(column=3, row=2, padx=50, pady=50)

# new_input.pack()

button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1, padx=50, pady=50)
# button.pack()

# New button for practice purposes
button2 = Button(text="Also click me!", command=button_2_clicked)
button2.grid(column=2, row=0, padx=50, pady=50)

# Text box
text = Text(height=5, width=30)
text.focus()
text.insert(END, "This is a test.")

# 1.0 meaning getting the text beginning with the first character from the first line of text
print(text.get("1.0", END))
# text.grid(column=1, row=1)
# text.pack()


# Spinbox
def spin_box():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spin_box)
# spinbox.pack()


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()


# Will print 1 if On button is clicked otherwise 0
def check_button():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is on or off", variable=checked_state, command=check_button)
checked_state.get()


# Radio button
def radio_button_used():
    print(radio_button_state.get())


radio_button_state = IntVar()
radio_1 = Radiobutton(text="Corn", value=1, variable=radio_button_state, command=radio_button_used)
radio_2 = Radiobutton(text="Pizza", value=2, variable=radio_button_state, command=radio_button_used)
# radio_1.pack()
# radio_2.pack()
# checkbutton.pack()


def list_box(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Pineapple", "Tomato", "Plum", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", list_box)
# listbox.pack()


print(window.grid_size())
window.mainloop()
