from tkinter import Tk, Canvas, Button, Label, PhotoImage
from math import floor

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25        
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_MARK = "✓"

reps = 0
window_counter = None

def reset():
    global reps
    reps = 0
    window.after_cancel(window_counter)
    status_label.config(text="Timer")
    canvas.itemconfig(timer, text="00:00")
    tick_marks.config(text="")


def starter():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        counter(work_secs)
        status_label.config(text="Work")
    elif reps % 8 == 0:
        counter(long_break_secs)
        status_label.config(text="Break", fg=RED)
    else:
        counter(short_break_secs)
        status_label.config(text="Break", fg=PINK)

def counter(count):
    global reps

    count_min = floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        canvas.itemconfig(timer, text=f"{count_min}:0{count_sec}")
    else:
        canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")

    if count > 0:
        global window_counter
        window_counter = window.after(1000, counter, count - 1)   
    else:
        starter()
        if reps % 2 == 0:
            tick_marks.config(text=f"{TICK_MARK}" * (reps // 2))



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

status_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
status_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=starter)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

tick_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
tick_marks.grid(row=3, column=1)

window.mainloop()