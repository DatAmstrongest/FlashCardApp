from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"

TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

flipped_card = None
words_to_learn = []
chosen_word = None


def read_data():
    try:
        df = pandas.read_csv("./data/words_to_learn.csv")
    except:
        df = pandas.read_csv("./data/french_words.csv")
    return df.to_dict(orient="records")


french_dict = read_data()
print(french_dict)


def choose_random():
    return random.choice(french_dict)


def wrong_button_action():
    assign_word()


def right_button_action():
    global french_dict
    french_dict = [x for x in french_dict if x["French"] != chosen_word["French"]]
    assign_word()


def assign_word():
    global flipped_card, chosen_word
    window.after_cancel(flipped_card)
    chosen_word = random.choice(french_dict)

    canvas.itemconfigure(card_image, image=card_front_img)
    canvas.itemconfigure(card_word, text=chosen_word["French"], fill=BLACK_COLOR)
    canvas.itemconfigure(card_title, text="French", fill=BLACK_COLOR)

    flipped_card = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfigure(card_image, image=card_back_img)
    canvas.itemconfig(card_word, fill=WHITE_COLOR, text=chosen_word["English"])
    canvas.itemconfig(card_title, fill=WHITE_COLOR, text="English")


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipped_card = window.after(3000, flip_card)

canvas = Canvas(
    width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR
)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front_img)
card_word = canvas.create_text(400, 263, text="", font=TITLE_FONT, fill=BLACK_COLOR)
card_title = canvas.create_text(400, 150, text="", font=WORD_FONT, fill=BLACK_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(
    image=right_button_img,
    highlightbackground=BACKGROUND_COLOR,
    command=right_button_action,
)
right_button.grid(column=0, row=1)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(
    image=wrong_button_img,
    highlightbackground=BACKGROUND_COLOR,
    command=wrong_button_action,
)
wrong_button.grid(column=1, row=1)

assign_word()

window.mainloop()


df = pandas.DataFrame(french_dict)
df.to_csv("./data/words_to_learn.csv", index=False)
