from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- VARIABLES ------------------------------- #
json_file_path = "Day_30\data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    import random
    import string
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
    try:
        if rnd_psswd == rnd_psswd:
            passwd_input.delete(0,END)
    except:
        passwd_input.delete(0,END)
        rnd_psswd = ""
        for char in password_list:
            rnd_psswd += char
        passwd_input.insert(0, rnd_psswd)
        pyperclip.copy(rnd_psswd) # copy to clipboard
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    passwd = passwd_input.get()
    new_data = {
        website: {
            "email": username,
            "password": passwd,
        }
    }
    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try: #Tente
            with open(json_file_path, "r") as data_file:
                # Read the old data file
                data = json.load(data_file)      
        except FileNotFoundError: #Se Encontrar esse erro faça isso:
            with open(json_file_path, "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else: #Senão encontrar um erro faça isso
            # Update the old data file with the new data
            data.update(new_data)
            with open(json_file_path, "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0,END)
            passwd_input.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_passwd():
    website = website_input.get()
    try:
        with open(json_file_path) as data_file:
            data= json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No json file Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day_30\logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

# ---------------------------- Labels'n Buttons ------------------------------- #

website_label = Label(text="Website:").grid(column=0, row=1)
username_label = Label(text="Email/Username:").grid(column=0, row=2, padx=10)
passwd_label = Label(text="Password:").grid(column=0, row=3)
# passwd_label = Label(text="Developed by Mateus Fonseca.").grid(column=0, row=6)

# ------------------------------- Entries ---------------------------- #

website_input = Entry(width=33)
website_input.grid(column=1,row=1)
website_input.focus()

username_input = Entry(width=33)
username_input.grid(column=1,row=2, columnspan=2,sticky=EW)
username_input.insert(0, "email@email.com")

passwd_input = Entry(width=33)
passwd_input.grid(column=1,row=3)

# ----------------------------- Buttons -------------------------------#

search_button = Button(text="Search", width=12, command=find_passwd).grid(column=2, row=1,sticky=W)

gen_button = Button(text="Gen Psswd", width=12, command=generate)
gen_button.grid(column=2, row=3,sticky=W)

add_button = Button(text="Add", width=25, command=save)
add_button.grid(column=1, row=4, columnspan=2,pady=5,padx=10 ,sticky=W)

window.mainloop()