from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time
from functions_and_lists import collides_with_paddle, BRICK_POSITIONS

all_bricks = []

screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

for i in range(0, len(BRICK_POSITIONS)):
    new_brick = Brick(BRICK_POSITIONS[i])
    all_bricks.append(new_brick)

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    scoreboard.write_score()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.x_bounce()

    if ball.ycor() > 280:
        ball.y_bounce()

    if collides_with_paddle(ball, paddle) and ball.ycor() == -180:
        ball.y_bounce()

    if ball.xcor() < -110:
        scoreboard.game_over()
        game_is_on = False

    if len(all_bricks) == 0:
        scoreboard.win()

    for brick in all_bricks:
        if ball.distance(brick) < 25:
            scoreboard.score += 1
            scoreboard.write_score()
            all_bricks.remove(brick)
            brick.goto(10000, 18832382)
            ball.y_bounce()
            ball.x_bounce()

screen.exitonclick()
