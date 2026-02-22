import tkinter
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
flip_timer = None 
chosen_dutch_word = None 

# ---------------------------- DATA ------------------------------- #
data_path_1 = "Day 31/flash-card-app/data/dutch_words.csv"
data_path_2 = "Day 31/flash-card-app/data/words_to_learn.csv"

df = pd.read_csv(data_path_1)
dutch_dict = df.to_dict(orient="records")

def choose_word_dutch():
    global chosen_dutch_word, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)
    
    #chosen_dutch_word=random.choice(list(dutch_dict.keys()))
    chosen_dutch_word=random.choice(dutch_dict)
    canvas.itemconfig(canvas_image,image=Q_img)
    canvas.itemconfig(language_title,text = "Dutch",fill = "black")
    canvas.itemconfig(word_to_learn,text = chosen_dutch_word["dutch"],fill = "black")

    flip_timer = window.after(5000,flip_card)

def flip_card():
    canvas.itemconfig(canvas_image,image=A_img)
    canvas.itemconfig(language_title,text = "English",fill="white")
    canvas.itemconfig(word_to_learn,text = chosen_dutch_word["english"],fill="white")


def known_words():
    global chosen_dutch_word

    if os.path.exists(data_path_2):
        wrong_df = pd.read_csv(data_path_2)
        wrong_words_dict = wrong_df.to_dict(orient="records")

        if chosen_dutch_word in wrong_words_dict:
            wrong_words_dict.remove(chosen_dutch_word)

        pd.DataFrame(wrong_words_dict,columns=["dutch", "english"]).to_csv(data_path_2,index=False)
    
    choose_word_dutch()

# ---------------------------- WRONG WORDS ------------------------------- #    
def unknown_words():
    global chosen_dutch_word

    if os.path.exists(data_path_2):
        wrong_df = pd.read_csv(data_path_2)
        wrong_words_dict = wrong_df.to_dict(orient="records")
    else:
        wrong_words_dict = []    

    if chosen_dutch_word not in wrong_words_dict:
        wrong_words_dict.append(chosen_dutch_word)

    pd.DataFrame(wrong_words_dict,columns=["dutch", "english"]).to_csv(data_path_2,index=False)
    
    choose_word_dutch()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width = 1000, height = 550,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
Q_img = tkinter.PhotoImage(file="Day 31/flash-card-app/images/card_front.png")
A_img = tkinter.PhotoImage(file="Day 31/flash-card-app/images/card_back.png")
canvas_image = canvas.create_image(500,300,image=Q_img)
word_to_learn = canvas.create_text(500, 300, text="Let's learn",font=(FONT_NAME,60,"bold"))
language_title = canvas.create_text(500, 180, text="Chosen Language",font=(FONT_NAME,40,"italic"))
canvas.grid(column=0,row=0,columnspan=2)


#Buttons
image_yes = tkinter.PhotoImage(file="Day 31/flash-card-app/images/right.png")
button_yes = tkinter.Button(image=image_yes,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,highlightthickness=0,command=known_words)
button_yes.grid(column=0,row=1)

image_no = tkinter.PhotoImage(file="Day 31/flash-card-app/images/wrong.png")
button_no = tkinter.Button(image=image_no,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,highlightthickness=0,command=unknown_words)
button_no.grid(column=1,row=1)

choose_word_dutch()
window.mainloop()

