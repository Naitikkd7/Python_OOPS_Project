from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0

        self.scoreboard = Turtle(visible=False)
        self.scoreboard.penup()
        self.scoreboard.color("white")
        self.scoreboard.speed("fastest")
        self.update_scoreboard()

        self.message = Turtle(visible=False)
        self.message.penup()
        self.message.color("white")
        self.message.speed("fastest")

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.goto(0, 310)
        self.scoreboard.write(
            f"Score: {self.score}",
            align="center",
            font=("Courier", 18, "bold"),
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.message.clear()
        self.message.goto(0, 0)
        self.message.write(
            f"GAME OVER\nFinal score: {self.score}",
            align="center",
            font=("Courier", 24, "bold"),
        )
