import tkinter
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- OPEN DATA ------------------------------- #
data_path = "Day 31/flash-card-app/data/dutch_words.csv"
df = pd.read_csv(data_path)
dutch_dict ={row.dutch:row.english for (index,row) in df.iterrows()}
print(dutch_dict)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width = 1000, height = 550,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
Q_img = tkinter.PhotoImage(file="Day 31/flash-card-app/images/card_front.png")
canvas.create_image(500,300,image=Q_img)
canvas.grid(column=0,row=0,columnspan=2)

#Buttons
image_yes = tkinter.PhotoImage(file="Day 31/flash-card-app/images/right.png")
button_yes = tkinter.Button(image=image_yes,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,highlightthickness=0)
button_yes.grid(column=0,row=1)

image_no = tkinter.PhotoImage(file="Day 31/flash-card-app/images/wrong.png")
button_no = tkinter.Button(image=image_no,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,highlightthickness=0)
button_no.grid(column=1,row=1)

window.mainloop()

