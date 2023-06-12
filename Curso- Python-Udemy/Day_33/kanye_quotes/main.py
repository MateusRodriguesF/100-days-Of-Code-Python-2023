from tkinter import *
import requests

def get_quote():
    # pass
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()["quote"]
    found_error = f"Error: {response}"
    if response.status_code != 200:
        canvas.itemconfig(quote_text, text=found_error)
    else:
        canvas.itemconfig(quote_text, text=quote, font=(20), fill="black")



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"Day_33\kanye_quotes\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"Day_33\kanye_quotes\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()