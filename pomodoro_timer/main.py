from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    check_mark_lable.config(text="")
    title_lable.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_breaks_sec = SHORT_BREAK_MIN * 60
    long_breaks_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_breaks_sec)
        title_lable.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_breaks_sec)
        title_lable.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_lable.config(text="Work", fg=GREEN)
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
                mark += "✔"
        check_mark_lable.config(text=mark)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds in range(0, 10):
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes.__round__(1)}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


title_lable = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
title_lable.grid(column=1,row=0)

check_mark_lable = Label(font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW)
check_mark_lable.grid(column=1,row=3)

start_button = Button(text="Start", command=start_timer, bg=YELLOW, borderwidth=0, highlightthickness=0, highlightbackground=YELLOW)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", bg=YELLOW, borderwidth=0, highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2,row=2)

window.mainloop()

