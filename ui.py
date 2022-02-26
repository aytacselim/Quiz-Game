from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.root = Tk()
        self.root.title("Quizlet")
        self.root.config(pady=20, padx=20, bg=THEME_COLOR)
        #Score Label
        self.score_label = Label(
            text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
            bg=THEME_COLOR,
            fg="white",
            font=("Ariel", 20, "italic"))
        self.score_label.grid(row=0, column=1)
        #Text Canvas
        self.text_canvas = Canvas(width=300, height=250)
        self.text_canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.question = self.text_canvas.create_text(
            150,
            125,
            width=280,
            text="questio12n",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"))
        #Buttons
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=false_img, borderwidth=0, bg=THEME_COLOR, command=self.guess_false)
        self.false_button.grid(row=2, column=1)
        self.true_button = Button(image=true_img, borderwidth=0, bg=THEME_COLOR, command=self.guess_true)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.text_canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.text_canvas.itemconfig(self.question, text=q_text)
        else:
            self.text_canvas.itemconfig(self.question, text="You've completed the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guess_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def guess_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.text_canvas.config(bg="green")
        else:
            self.text_canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)

