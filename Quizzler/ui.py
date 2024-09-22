from tkinter import Tk, Label, Canvas, PhotoImage, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

	def __init__(self, quiz: QuizBrain):
		self.quiz = quiz 

		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(bg=THEME_COLOR, padx=20, pady=20)

		self.score_label = Label(text="Score: 0", fg="white")
		self.score_label.config(bg=THEME_COLOR)
		self.score_label.grid(row=0, column=1)

		self.canvas = Canvas(width=300, height=250)
		self.question = self.canvas.create_text(150, 125, text="Question!", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
		self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

		true_image = PhotoImage(file="images/true.png")
		self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
		self.true_button.grid(row=2, column=0)

		false_image = PhotoImage(file="images/false.png")
		self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
		self.false_button.grid(row=2, column=1)

		self.generate_question()

		self.window.mainloop()
		
	def generate_question(self):
		self.canvas.config(bg="white")
		if self.quiz.still_has_questions():
			self.canvas.config(bg="white")
			self.score_label.config(text=f"Score: {self.quiz.score}")
			gen_question = self.quiz.next_question()
			self.canvas.itemconfig(self.question, text=gen_question)
		else:
			self.canvas.itemconfig(self.question, text="Quiz is over bud.")
			self.true_button.config(state="disabled")
			self.false_button.config(state="disabled")

	def true_pressed(self):
		self.quiz.check_answer("True")
		self.give_feedback(True)

	def false_pressed(self):
		self.quiz.check_answer("False")
		self.give_feedback(False)

	def give_feedback(self, is_right):
		if is_right:
			self.canvas.config(bg="green")
		else:
			self.canvas.config(bg="red")
		self.window.after(2000, self.generate_question)