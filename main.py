from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"

TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(
    width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR
)

card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=0, row=1)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=1)

title_label = Label(text="Title", bg=WHITE_COLOR, fg=BLACK_COLOR, font=TITLE_FONT)
title_label.place(x=360, y=150)

word_label = Label(text="Word", bg=WHITE_COLOR, fg=BLACK_COLOR, font=WORD_FONT)
word_label.place(x=325, y=263)

window.mainloop()
