import tkinter

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 300)
window.config(padx = 20,pady = 20)

# Label
my_label = tkinter.Label(text = "I am a Label",font=("Arial",24,"bold"))

# Layouts
#my_label.pack(side = "top")
#my_label.place(x=0,y=0)
my_label.grid(column=0,row=0)

# my_label.config(text="New Text")

# Button
button = tkinter.Button(text="Click me",command=button_clicked)
#button.pack()
button.grid(column = 10, row = 0)

# Entry (Input)

input = tkinter.Entry(width=10)
print(input.get())
#input.pack()
input.grid(column = 3, row = 5)

window.mainloop()