from turtle import Screen, Turtle

snake = Turtle()
screen = Screen()

# set screen visuals and create snake body
screen.bgcolor("black")
screen.screensize(canvwidth=600,canvheight=600)
snake.color("white")
snake.shape("square")
snake.shapesize(stretch_wid=1, stretch_len=3)

# Move snake
def move(game_over):
    while not game_over:
        snake.forward(10)

def turn_right():
    """The snake will turn right from its current position."""
    snake.right(90)

def turn_left():
    """The snake will turn left from its current position."""
    snake.left(90)

def begin_game():
    move()

screen.onkey(key = "enter", fun = begin_game)
#screen.onkey(key="space",fun=move)
screen.onkey(key = "a",fun = turn_left)
screen.onkey(key = "d",fun = turn_right)

#----------------------------
screen.listen()
screen.exitonclick()