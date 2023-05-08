from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- Var ------------------------------- #
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        canvas.itemconfig(timer_text, fill=RED)
        label_timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        canvas.itemconfig(timer_text, fill=PINK)
        label_timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        canvas.itemconfig(timer_text, fill=GREEN)
        label_timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # to change a canvas you have to use canvas.itemconfig()
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "🗸"
        label_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=90, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Day_28\tomato.png")
canvas.create_image(100,112, image=tomato_img,)
timer_text = canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME,28,"bold"))
canvas.grid(column=1, row=1)


label_timer = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,"bold"))
label_timer.grid(column=1, row=0)

label_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,16,"bold"))
label_check.grid(column=1, row=3)

start_button = Button(text="Start", bg=YELLOW, font=("Arial",12,"bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, font=("Arial",12,"bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()