from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.setup_ui()
        self.get_next_question()
        self.window.mainloop()

    def setup_ui(self):
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canwas = Canvas()
        self.canwas.config(bg="white", width=300, height=250)
        self.question_text = self.canwas.create_text(150,125,
                                                     text="Some question text",
                                                     width=280,
                                                     fill=THEME_COLOR, font=("Arian", 25, "normal"))
        self.canwas.grid(column=0, row=1, columnspan = 2, pady=50)


        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row = 2)

        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2 )

    def get_next_question(self):
        self.canwas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canwas.itemconfig(self.question_text, text= next_question)
        else:
            self.canwas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canwas.config(bg="green")

        else:
            self.canwas.config(bg="red")
        self.window.after(1000, self.get_next_question)




