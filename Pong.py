# Simple Pong (ATARI like) in Python 3 (beginner level)
# By FreeCodeCamp <https://www.youtube.com/watch?v=XGf2GcyHPhc>
# Part 1: Getting Started

# Its like a pygame but for begginers
import turtle  # A python module

wn = turtle.Screen()
wn.title("Pong by @TonyNunes") # the title of the screen
wn.bgcolor("black") # Background color
wn.setup(width=800, height=600)  # Size 
wn.tracer(0) # Stop window from updating, so with it disabled, we have to manually update the screen. Now we can speed up the game

# Components of the game

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')

paddle_a.color('#127FE5')

# by default the size is 20x20 px
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # stretch takes the default size and multiple by the given value, in this case 5 and 1
paddle_a.penup()
paddle_a.goto(-390, 0)

'''=============================================================='''

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('#FA3029')

# by default the size is 20x20 px
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # stretch takes the default size and multiple by the given value, in this case 5 and 1
paddle_b.penup()
paddle_b.goto(380, 0)

'''=============================================================='''

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')

# by default the size is 20x20 px
ball.penup()
ball.goto(0, 0)

# *** Components of the game

'''=============================================================='''

# Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

'''=============================================================='''



'''=============================================================='''
# Main game loop
while True:
    wn.update() # Now every time the loop starts, the windows is updated