from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day 24/snake_game_highest_score/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}   Hight Score : {self.high_score}",align = ALIGNMENT ,font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day 24/snake_game_highest_score/data.txt",mode = 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align = ALIGNMENT ,font = FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
        

