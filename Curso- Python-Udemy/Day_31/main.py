# ------------------------- IMPORTS --------------------------- #
from tkinter import *
# from tkinter import messagebox
import pandas as pd
import random
# ----------------------- VARIABLES & CONSTANTS --------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pd.read_csv(r"Day_31\data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(r"Day_31\data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ----------------------- Change the Card --------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(r"Day_31\data\words_to_learn.csv", index=False)
    next_card()
# ----------------------- UI SETUP -----------------------------#
window  = Tk()
window.title("Flashy Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=r"Day_31\images\card_front.png")
card_back_img = PhotoImage(file=r"Day_31\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)# To remove white area around the image 
canvas.grid(column=0, row=0, columnspan=2)
# --------------------------- BUTTONS --------------------------#
right_btn_img= PhotoImage(file=r"Day_31\images\right.png")
wrong_btn_img = PhotoImage(file=r"Day_31\images\wrong.png")
right_btn = Button(image=right_btn_img, highlightthickness=0, background=BACKGROUND_COLOR,command=is_known)
right_btn.grid(column=1, row=1)
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, background=BACKGROUND_COLOR,command=next_card)
wrong_btn.grid(column=0, row=1)
next_card()
window.mainloop()