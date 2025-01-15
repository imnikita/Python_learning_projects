from tkinter import *
from random import randint, choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

words_data_frame = {}

try:
    words_data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data_frame = pandas.read_csv("data/french_words.csv")

to_learn = words_data_frame.to_dict(orient="records")
current_card = {}

def show_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    show_next_card()

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)

# SETUP UI
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_image, highlightthickness=0, command=show_next_card)
unknown_button.grid(row= 1, column=0)

check_button_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_image, highlightthickness=0, command=is_known)
check_button.grid(row= 1, column=1)

show_next_card()

window.mainloop()

