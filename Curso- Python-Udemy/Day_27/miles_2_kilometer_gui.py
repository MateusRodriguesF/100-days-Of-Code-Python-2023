from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=150)
window.config(padx=10, pady=20)

def convert():
    mile = float(input_text.get())
    nw_rsult = round(mile * 1.6)
    label_result["text"] = nw_rsult


label_eq = Label(text="is equal to >", font=("System", 18, "normal"))
label_eq.grid(column=0, row=2)

label_mile = Label(text="< Miles", font=("System", 18, "normal"))
# label_mile.config(padx=-10, pady=20)
label_mile.grid(column=3, row=1)

label_km = Label(text="< Km", font=("System", 18, "normal"))
# label_km.config(padx=1, pady=0)
label_km.grid(column=3, row=2)


label_result = Label(text=0, font=("System", 18, "normal"))
label_result.grid(column=2, row=2)

credit = Label(text="Coded by Mateus R Fonseca", font=("System", 6, "bold"))
credit.config(padx=0, pady=6)
credit.grid(column=3, row=3)

calc_button = Button(text="Calculate", command=convert, font=("System", 16, "normal"))
calc_button.grid(column=2, row=3)

input_text = Entry(width=7, font=("System", 18, "normal"))
input_text.insert(END, string=0)
input_text.grid(column=2, row=1)


window.mainloop()