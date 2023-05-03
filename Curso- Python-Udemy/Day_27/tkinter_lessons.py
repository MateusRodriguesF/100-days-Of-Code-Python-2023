from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # add padding to the window

def button_clicked():
    new__text = input_text.get()
    my_label["text"] = new__text
    # button["text"] = "I got Clicked"

# Label
my_label = Label(text="I am a Label.", font=("Arial", 24, "bold"))
# Another ways to set the label text
# my_label["text"] = "I am a Label text"
# my_label.config(text="Other label Text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)


# Button 
button = Button(text="Click me!", command=button_clicked)
# button.pack() # put the element in the center of the screen
# button.place(x=0, y=0) # Put the element Precisely in a position
button.grid(column=1, row=1) # put the element in a grid position

#New button
new_button = Button(text="New!", command=button_clicked)
new_button.grid(column=2, row=0)

# Input
input_text = Entry()
# input_text.pack()
input_text.grid(column=3, row=2) 


window.mainloop()