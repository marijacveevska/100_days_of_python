import tkinter
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizzInterface():

    def __init__(self,quiz_brain:QuizBrain):

        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        #Canvas
        self.canvas = tkinter.Canvas(width = 300, height = 250, bg="white")
        #Questions
        self.question_text = self.canvas.create_text(150,125,width=280,text="Queston text",font=(FONT_NAME,20))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)


        #Buttons
        image_yes = tkinter.PhotoImage(file="Day 34/quizzler-app-GUI/images/true.png")
        self.button_yes = tkinter.Button(image=image_yes,bg=THEME_COLOR,highlightthickness=0,highlightbackground=THEME_COLOR,command=self.true_pressed)
        self.button_yes.grid(column=0,row=2)
        
        image_no = tkinter.PhotoImage(file="Day 34/quizzler-app-GUI/images/false.png")
        self.button_no = tkinter.Button(image=image_no,bg=THEME_COLOR,highlightthickness=0,highlightbackground=THEME_COLOR,command=self.false_pressed)
        self.button_no.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz")
            self.button_yes.config(state="disabled")
            self.button_no.config(state="disabled")


    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(500,self.get_next_question)


    