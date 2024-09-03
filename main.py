import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pang")
screen.tracer(0)  # to reset the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

def r_paddle_up():
    r_paddle.go_up()

def r_paddle_down():
    r_paddle.go_down()

def l_paddle_up():
    l_paddle.go_up()

def l_paddle_down():
    l_paddle.go_down()

screen.listen()
screen.onkey(r_paddle_up, "Up")
screen.onkey(r_paddle_down, "Down")
screen.onkey(l_paddle_up, "w")
screen.onkey(l_paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()
        scoreboard.increase_score()  # Increase score when the ball hits a paddle

    # Detect if ball goes out of bounds
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
