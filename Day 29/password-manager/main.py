import tkinter
from tkinter import messagebox
from password_generator import generated_password

BACKGROUND_COLOR = "#e9e7e1"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def add_gen_password():

    entry_password.insert(0,generated_password)
    
# ---------------------------- SAVE DATA ------------------------------- #

def add_to_file():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        return
    
    is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail : {username} \nPassword : {password} \nIs it ok to save?")

    if is_ok:
        with open("Day 29/password-manager/secret_file.txt",mode="a") as file:
            file.write(f"{website} | {username} | {password}\n")

        entry_website.delete(0, tkinter.END)
        entry_password.delete(0, tkinter.END)
        entry_website.focus()
    
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width = 150, height = 200,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
logo_img = tkinter.PhotoImage(file="Day 29/password-manager/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#Buttons
button_generate = tkinter.Button(text="Generate Password",bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,command=add_gen_password)
button_generate.grid(column=2,row=3)

button_add = tkinter.Button(text="Add",width=35,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR,command=add_to_file)
button_add.grid(column=1,row=4,columnspan=2)

#Labels
label_web = tkinter.Label(text="Website: ",bg=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
label_web.grid(column=0,row=1)

label_username = tkinter.Label(text="Email/Username:",bg=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
label_username.grid(column=0,row=2)

label_pass = tkinter.Label(text="Password:",bg=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
label_pass.grid(column=0,row=3)

#Entries
entry_website = tkinter.Entry(width=37,bg="#fffefc",highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
entry_website.grid(column=1,row=1,columnspan=2)
entry_website.focus()

entry_username = tkinter.Entry(width=37,bg="#fffefc",highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
entry_username.grid(column=1,row=2,columnspan=2)
entry_username.insert(0,"marija@email.com")

entry_password = tkinter.Entry(width=19,bg="#fffefc",highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
entry_password.grid(column=1,row=3)

window.mainloop()