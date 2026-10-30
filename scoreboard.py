from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, mid_x, y):
        super().__init__()
        self.mid_x = mid_x
        self.y = y
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.mid_x - 100, self.y)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(self.mid_x + 100, self.y)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()