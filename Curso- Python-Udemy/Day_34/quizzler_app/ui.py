from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):#calling the QuizBrain class 
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #------------------------ Label Score ----------------------------------------#
        self.score_label = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        #------------------------------ Canvas --------------------------------#
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        #------------------------------ Txt ----------------------------------#
        self.question_txt = self.canvas.create_text(
            150, 
            125,
            width=280,
            text="Test Text", 
            font=("Arial", 20, "italic"))
        
        #------------------------------ Buttons imgs -------------------------#

        true_img = PhotoImage(file="Day_34/quizzler_app/images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="Day_34/quizzler_app/images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2)

        #-------------------------------------------------------------------#
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_txt, text="You've reached the end of the quiz!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="blue")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)