from tkinter import *
import pandas as pd
import random
import logging
BACKGROUND_COLOR = "#B1DDC6"
#load small word list if in test mode
test = False

logger = logging.getLogger("flashcards")
logging.basicConfig (
    level="INFO"
)

# ----------------------------- initialize data structures --------------------------------- #
images = {"card_back": {}, "card_front": {}, "right": {}, "wrong": {}}
native_language = "english"
new_language = "italian"

#load test file if in test mode

try:
    data = pd.read_csv("data/words_to_learn.csv")
    logging.info("words to learn found and loaded")

except FileNotFoundError:
    if test:
        data = pd.read_csv("data/it-en1k.csv.test")
    else:
        data = pd.read_csv("data/it-en1k.csv")
    logging.info("words to learn file not found. loading base file.")

to_learn = data.to_dict(orient="records")

# ---------------------------- functions ---------------------------------- #
def next_card():
    global current_card, flip_timer
    # goofy tkinter stuff - need to reset the timer object
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=images["card_front"])
    canvas.itemconfig(card_title, text = new_language, fill="black")
    canvas.itemconfig(card_word, text=current_card[new_language], fill="black")
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=images["card_back"])
    canvas.itemconfig(card_title, text = native_language, fill="white")
    canvas.itemconfig(card_word, text=current_card[native_language], fill="white")

def is_known():
    #TODO check for empty list
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Learn Italian")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

#flip card after three seconds
flip_timer = window.after(3000, func=flip_card)

# create dictionary of image objects
for image in images:
    images[image] = PhotoImage(file=f"images/{image}.png")

#build canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400,263, image=images["card_front"])
card_title = canvas.create_text(400,150, fill="black", font=("Ariel", 40, "italic"))
card_word  = canvas.create_text(400, 263, fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#buttons
unknown_button = Button(image=images["wrong"], highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=images["right"],highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)




next_card()

window.mainloop()