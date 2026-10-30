from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, snake_positions=()):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed("fastest")
        self.current_color = (160, 220, 160)
        self.refresh(snake_positions)

    @staticmethod
    def random_color():
        # Always return integer RGB values for colormode(255).
        return (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255),
        )

    def refresh(self, snake_positions=()):
        occupied = {(round(x), round(y)) for x, y in snake_positions}

        # Keep food on the 20-pixel grid and inside the playable region.
        choices = [
            (x * 20, y * 20)
            for x in range(-13, 14)
            for y in range(-13, 14)
            if (x * 20, y * 20) not in occupied
        ]
        if not choices:
            return

        self.current_color = self.random_color()
        self.color(self.current_color)
        self.goto(random.choice(choices))
