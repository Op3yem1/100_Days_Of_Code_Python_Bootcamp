from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()

# set screen visuals and create snake body
screen.bgcolor("black")
screen.title("Snake Game")
screen.screensize(canvwidth=600,canvheight=600)
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.update()

at_food = False
score = 0
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    screen.onkey(key="Left",fun=snake.turn_left)
    screen.onkey(key="Right", fun=snake.turn_right)
    screen.onkey(key="Up",fun=snake.up)
    screen.onkey(key="Down",fun=snake.down)
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.appear()
        snake.grow()
        score += 1
    #screen.onkey(key="c",fun=food.appear)





#----------------------------

screen.exitonclick()