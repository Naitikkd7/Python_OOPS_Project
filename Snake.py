from numbers import Real
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def normalize_rgb_color(color):
    """Convert RGB tuples containing floats into safe integer RGB values.

    Turtle's default color mode is 1.0, while this game uses 255. This helper
    also safely handles colors returned by older versions of the food code.
    Named colors such as 'white' pass through unchanged.
    """
    if not isinstance(color, (tuple, list)) or len(color) != 3:
        return color

    if not all(isinstance(channel, Real) for channel in color):
        return color

    channels = [float(channel) for channel in color]

    # RGB values all in 0..1 are treated as normalized RGB values.
    if all(0.0 <= channel <= 1.0 for channel in channels):
        channels = [channel * 255 for channel in channels]

    return tuple(max(0, min(255, int(round(channel)))) for channel in channels)


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position, color="white"):
        segment = Turtle("square")
        segment.color(normalize_rgb_color(color))
        segment.penup()
        segment.speed("fastest")
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].position())
        self.segments[0].forward(MOVE_DISTANCE)

    def extend(self, color="white"):
        self.add_segment(self.segments[-1].position(), color)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
