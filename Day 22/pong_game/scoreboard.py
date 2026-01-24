from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}",align = ALIGNMENT ,font = FONT)
        self.goto(100,200)
        self.write(f"{self.r_score}",align = ALIGNMENT ,font = FONT)

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()
        
    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align = ALIGNMENT ,font = FONT)
