from tkinter import *
from tkinter import Tk
from tkinter import ttk
import math

# ---------------------------- CONSTANTS ------------------------------- #
LIGHTGRAY = "#EAEAEA"
GRAY = "#B2B2B2"
DARKGRAY = "#3C4048"
BLUE = "#00ABB3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_seconds = 10
    short_break_seconds = 10
    long_break_seconds = 10

    if reps % 2 != 0:
        countdown(work_seconds)
        timer_label.config(text="Work", foreground=BLUE)
    elif reps % 2 == 0 and reps < 7:
        countdown(short_break_seconds)
        timer_label.config(text="Break time!", foreground=BLUE)
    else:
        countdown(long_break_seconds)
        timer_label.config(text="Break time!", foreground=BLUE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        checkmark_label.config(text=u'\u2713' * reps)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=450, height=448)
window.config(padx=100, pady=50, bg=LIGHTGRAY)

timer_label = ttk.Label(text="Timer", font=("Courier", 40, "bold"), background=LIGHTGRAY, foreground=BLUE)
timer_label.pack(anchor="n")

canvas = Canvas(width=200, height=224, bg=LIGHTGRAY, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")

canvas.create_image(100, 112, image=tomato_image)

timer_text = canvas.create_text(100, 130, text="00:00", font=("Arial", 35, "bold"), fill="white")
canvas.pack()

start_button = ttk.Button(text="Start", width=5, command=start_timer)
start_button.pack(side="left", anchor="n")

reset_button = ttk.Button(text="Reset", width=5, command=reset_timer)
reset_button.pack(side="right", anchor="n")

checkmark_label = Label(window, text=u'\u2713', background=LIGHTGRAY, foreground=BLUE, font=24)
checkmark_label.pack(pady=20)

window.mainloop()
