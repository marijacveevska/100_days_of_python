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
reps = 0
timer = None

def bring_window_to_front():
    window.deiconify()       # In case minimized
    window.lift()            # Bring to front
    window.attributes("-topmost", True)
    window.after(1000, lambda: window.attributes("-topmost", False))


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text ="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text = "Long Break",fg = RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text = "Short Break",fg = PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text = "Work Time",fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(t):
    count_min = math.floor(t/60)
    count_sec = t % 60 
    if 0 <= count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text =f"{count_min}:{count_sec}")

    if reps % 2 != 0 and t == 5 * 60:
        bring_window_to_front()


    if t > 0:
        global timer
        timer = window.after(1000,countdown,t-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
# window.minsize(width = 250, height = 100)
window.config(padx = 100,pady = 50,bg=YELLOW)

timer_label = tkinter.Label(text="Timer",font=(FONT_NAME,40),bg=YELLOW,fg=GREEN)
timer_label.grid(column=1,row=0)

check_label = tkinter.Label(bg=YELLOW,fg=GREEN)
check_label.grid(column=1,row=3)

button_start = tkinter.Button(text="Start",highlightbackground=YELLOW, highlightcolor=YELLOW,command=start_timer)
button_start.grid(column=0,row=2)

button_reset = tkinter.Button(text="Reset",highlightbackground=YELLOW, highlightcolor=YELLOW, command=reset_timer)
button_reset.grid(column=2,row=2)

canvas = tkinter.Canvas(width = 200, height = 224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="Day 28/pomodoro-app/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


window.mainloop()

# ✔