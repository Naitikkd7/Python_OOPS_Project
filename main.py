from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

LEFT_X, RIGHT_X = -187, 574
TOP_Y, BOTTOM_Y = 145, -535
MID_X = (LEFT_X + RIGHT_X) // 2
MID_Y = (TOP_Y + BOTTOM_Y) // 2

screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((RIGHT_X, MID_Y))
l_paddle = Paddle((LEFT_X, MID_Y))
ball = Ball((MID_X, MID_Y))
scoreboard = Scoreboard(MID_X, TOP_Y - 60)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    
    if ball.ycor() > TOP_Y or ball.ycor() < BOTTOM_Y:
        ball.bounce_y()

   
    if (ball.distance(r_paddle) < 50 and ball.xcor() > RIGHT_X - 34) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < LEFT_X + 32):
        ball.bounce_x()

    
    if ball.xcor() > RIGHT_X + 20:
        ball.reset_position()
        scoreboard.l_point()

   
    if ball.xcor() < LEFT_X - 18:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()