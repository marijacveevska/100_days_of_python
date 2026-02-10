import tkinter
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(t):
    count_min = math.floor(t/60)
    count_sec = t % 60 

    canvas.itemconfig(timer_text,text =f"{count_min}:{count_sec}")
    if t > 0:
        window.after(1000,countdown,t-1)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
# window.minsize(width = 250, height = 100)
window.config(padx = 100,pady = 50,bg=YELLOW)

timer_text = tkinter.Label(text="Timer",font=(FONT_NAME,40),bg=YELLOW,fg=GREEN)
timer_text.grid(column=1,row=0)

check_label = tkinter.Label(text="✔",bg=YELLOW,fg=GREEN)
check_label.grid(column=1,row=3)

button_start = tkinter.Button(text="Start",highlightbackground=YELLOW, highlightcolor=YELLOW,command=start_timer)
button_start.grid(column=0,row=2)

button_reset = tkinter.Button(text="Reset",highlightbackground=YELLOW, highlightcolor=YELLOW)
button_reset.grid(column=2,row=2)

canvas = tkinter.Canvas(width = 200, height = 224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="Day 28/pomodoro-app/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


window.mainloop()

# ✔