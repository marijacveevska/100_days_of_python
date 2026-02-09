import tkinter

def calculate_km():
    new_text = round(float(miles.get()) * 1.60934,2)
    text4.config(text=new_text)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width = 250, height = 100)
window.config(padx = 20,pady = 20)

text1 = tkinter.Label(text = "Miles",font=("Calibri",12))
text1.grid(column=3,row=0)

text2 = tkinter.Label(text = "Km",font=("Calibri",12))
text2.grid(column=3,row=1)

text3 = tkinter.Label(text = "is equal to",font=("Calibri",12))
text3.grid(column=0,row=1)

text4 = tkinter.Label(text = "0",font=("Calibri",12))
text4.grid(column=1,row=1)

button = tkinter.Button(text="Calculate",command=calculate_km)
button.grid(column = 1, row = 2)

miles = tkinter.Entry(width=7)
print(miles.get())
miles.grid(column = 1, row = 0)


window.mainloop()