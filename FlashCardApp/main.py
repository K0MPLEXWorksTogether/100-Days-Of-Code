from tkinter import Tk, Canvas, PhotoImage, Button

import random
import pandas

def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(DATAFRAME_DICT)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(guess_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card, image=flash_card_front)
    flip_timer = window.after(TIME, flip)

def flip():
    global current_word
    meaning = current_word["English"]
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(guess_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card, image=flash_card_back)

def is_known():
    DATAFRAME_DICT.remove(current_word)
    learn = pandas.DataFrame(DATAFRAME_DICT)
    learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

BACKGROUND_COLOR = "#B1DDC6"
try:
    DATAFRAME = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    DATAFRAME = pandas.read_csv("data/french_words.csv")
    DATAFRAME_DICT = DATAFRAME.to_dict(orient="records")
else:
    DATAFRAME_DICT = DATAFRAME.to_dict(orient="records")
TIME = 3000

current_word = None

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_front = PhotoImage(file="images/card_front.png")
flash_card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=flash_card_front)
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
guess_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()