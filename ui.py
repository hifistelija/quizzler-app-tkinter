from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Sample text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Buttons
        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0,
                                   command=lambda: self.guess_answer("False"))
        self.button_false.grid(row=2, column=1)

        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0,
                                  command=lambda: self.guess_answer("True"))
        self.button_true.grid(row=2, column=0)

        self.button_restart = Button(text="Restart", command=self.restart_game)
        self.button_restart.grid(row=0, column=0)
        # Labels
        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def guess_answer(self, guess):
        is_correct = self.quiz.check_answer(guess)
        if is_correct:
            self.canvas.config(bg="green")
            self.quiz.score += 1
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_question, text="You've reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def restart_game(self):
        self.quiz.restart_quiz()
        self.label_score.config(text="Score: 0")
        self.get_next_question()
        self.button_true.config(state="normal")
        self.button_false.config(state="normal")
