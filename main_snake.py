from turtle import Screen, Turtle

from Snake import Snake
from food import Food
from scoreboard import Score

# Window and play area use the same turtle-coordinate system.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
WORLD_LEFT = -400
WORLD_RIGHT = 400
WORLD_BOTTOM = -350
WORLD_TOP = 350
WALL_X = 350
WALL_Y = 280
MOVE_DELAY_MS = 120

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.colormode(255)  # Set before creating any objects with RGB colors.
screen.tracer(0)
screen.setworldcoordinates(
    WORLD_LEFT, WORLD_BOTTOM, WORLD_RIGHT, WORLD_TOP
)

snake = Snake()
food = Food([segment.position() for segment in snake.segments])
score = Score()

prompt = Turtle(visible=False)
prompt.penup()
prompt.color("white")
prompt.goto(0, 0)
prompt.write(
    "Press an arrow key to start",
    align="center",
    font=("Courier", 16, "bold"),
)

started = False
game_over = False


def start_game_with(direction_method):
    """Set the requested direction, then start the timer loop once."""
    global started
    if game_over:
        return

    direction_method()
    if not started:
        started = True
        prompt.clear()
        screen.update()
        screen.ontimer(game_loop, MOVE_DELAY_MS)


def start_up():
    start_game_with(snake.up)


def start_down():
    start_game_with(snake.down)


def start_left():
    start_game_with(snake.left)


def start_right():
    start_game_with(snake.right)


def game_loop():
    global game_over
    if game_over or not started:
        return

    try:
        snake.move()
        head = snake.segments[0]

        # Eat food: use the stored, integer RGB color rather than asking
        # Turtle for a color representation that may contain floats.
        if head.distance(food) < 17:
            eaten_color = food.current_color
            snake.extend(eaten_color)
            score.increase_score()
            occupied = [segment.position() for segment in snake.segments]
            food.refresh(occupied)

        # Wall collision.
        if abs(head.xcor()) > WALL_X or abs(head.ycor()) > WALL_Y:
            game_over = True
            score.game_over()

        # Self collision.
        if not game_over:
            for segment in snake.segments[1:]:
                if head.distance(segment) < 10:
                    game_over = True
                    score.game_over()
                    break

        screen.update()

    except Exception as error:
        # Keep the failure visible in the terminal instead of silently
        # leaving a frozen Turtle window during development.
        print("An error occurred in the Snake Game loop:", repr(error))
        raise

    if not game_over:
        screen.ontimer(game_loop, MOVE_DELAY_MS)


screen.listen()
screen.onkey(start_up, "Up")
screen.onkey(start_down, "Down")
screen.onkey(start_left, "Left")
screen.onkey(start_right, "Right")

screen.update()
screen.mainloop()
