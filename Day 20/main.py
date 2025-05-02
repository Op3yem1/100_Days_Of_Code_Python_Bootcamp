from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()

# set screen visuals and create snake body
screen.bgcolor("black")
screen.title("Snake Game")
screen.screensize(canvwidth=600,canvheight=600)
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()
screen.listen()
screen.update()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    snake.head_move()
    screen.onkey(key="Left",fun=snake.turn_left)
    screen.onkey(key="Right", fun=snake.turn_right)
    screen.onkey(key="Up",fun=snake.up)
    screen.onkey(key="Down",fun=snake.down)




#----------------------------

screen.exitonclick()