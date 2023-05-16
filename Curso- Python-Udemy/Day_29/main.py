from tkinter import *
from tkinter import messagebox
import pyperclip
FONT_NAME = "System"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    import random
    import string
    from time import sleep

    letters_low = list(string.ascii_lowercase)
    letters_up = list(string.ascii_uppercase)
    numbers = range(0,10)
    symbols = ["*", "@", "#", "$", "%", "&", "!", "?"]

    password_list = []
    for char in range(3):
        password_list.append(random.choice(letters_up))
        password_list.append(random.choice(letters_low))
        password_list.append(str(random.choice(numbers)))
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    # Final Result
    rnd_psswd = ""
    for char in password_list:
        rnd_psswd += char
    passwd_input.insert(0, rnd_psswd)
    pyperclip.copy(rnd_psswd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    passwd = passwd_input.get()

    if website == "" or username == "" or passwd == "":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nE-mail: {username}"
                            f"\nPassword: {passwd} \nIs it Ok to save?")
        if is_ok:
            with open(r"Day_29\data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {passwd}\n")
                website_input.delete(0,END)
                passwd_input.delete(0,END)
                username_input.delete(0,END)
                username_input.insert(0, "email@email.com")
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day_29\logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

# ---------------------------- Labels'n Buttons ------------------------------- #

website_label = Label(text="Website:").grid(column=0, row=1, sticky=W)
username_label = Label(text="Email/Username:").grid(column=0, row=2, sticky=W)
passwd_label = Label(text="Password:").grid(column=0, row=3, sticky=W)
passwd_label = Label(text="Developed by Mateus Fonseca.").grid(column=0, row=6, sticky=W)

# ------------------------------- Entries ---------------------------- #

website_input = Entry(width=35)
website_input.grid(column=1,row=1, columnspan=2, sticky=W)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1,row=2, columnspan=2, sticky=W)
username_input.insert(0, "email@email.com")

passwd_input = Entry(width=25)
passwd_input.grid(column=1,row=3, sticky=W)

# ----------------------------- Buttons -------------------------------#

gen_button = Button(text="Generate Password", justify=LEFT, command=generate)
gen_button.grid(column=2, row=3, sticky=W, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()