# Simple Pong (ATARI like) in Python 3 (beginner level)
# By FreeCodeCamp <https://www.youtube.com/watch?v=XGf2GcyHPhc>
# Part 1: Getting Started

# Its like a pygame but for begginers
import turtle  # A python module

import time

wn = turtle.Screen()
wn.title("Pong by @TonyNunes")  # the title of the screen
wn.bgcolor("black")  # Background color
wn.setup(width=800, height=600)  # Size
wn.tracer(
    0
)  # Stop window from updating, so with it disabled, we have to manually update the screen. Now we can speed up the game

"""=============================================================="""

# Components of the game

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")

paddle_a.color("#127FE5")

# by default the size is 20x20 px
paddle_a.shapesize(
    stretch_wid=5, stretch_len=1
)  # stretch takes the default size and multiple by the given value, in this case 5 and 1
paddle_a.penup()
paddle_a.goto(-380, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#FA3029")

# by default the size is 20x20 px
paddle_b.shapesize(
    stretch_wid=5, stretch_len=1
)  # stretch takes the default size and multiple by the given value, in this case 5 and 1
paddle_b.penup()
paddle_b.goto(370, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")

# by default the size is 20x20 px
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # d = delta(change/variation) | x axis
ball.dy = 0.2

# *** Components of the game

"""=============================================================="""

# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)


"""=============================================================="""

# Keyboard binding

wn.listen()  # listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


"""=============================================================="""
# Main game loop
while True:
    wn.update()  # Now every time the loop starts, the windows is updated

    # Move the ball
    if ball.xcor() == 0 and ball.ycor() == 0:
        time.sleep(0.5)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)



    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball colisions
    # for paddle_a
    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(350)
        ball.dx *= -1
    
    
    # for paddle_b
    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1
