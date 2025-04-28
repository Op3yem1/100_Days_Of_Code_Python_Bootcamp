from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

# Set screen visuals
screen = Screen()
screen.screensize(canvwidth=800,canvheight=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen_right_x = screen.screensize()[0]/2
screen_left_x = -screen_right_x
screen_top_y = screen.screensize()[1]/2
screen_bottom_y = -screen_top_y
screen.setup(width=screen.screensize()[0]+20,height=screen.screensize()[1]+20)
screen.tracer(0)

# Set up screen elements
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.update()

# Initialise game parameters
THRESHOLD = 15
at_food = False
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
    if snake.head.distance(food) < THRESHOLD:
        food.appear()
        snake.grow()
        score.increase_score()
        score.write_score()

    # Detect collision with wall or snake body
    if snake.head.xcor() > screen_right_x or snake.head.xcor() < screen_left_x or snake.head.ycor() > screen_top_y or snake.head.ycor() < screen_bottom_y:
        game_on = False
        score.game_over()
        print("collision with wall")

# Fix this buggy bit here
    if len(snake.segments) > 4:
        for seg in snake.segments[4:-1]:
            if abs(snake.head.xcor() - seg.xcor() < THRESHOLD) and abs(snake.head.ycor() - seg.ycor() < THRESHOLD):
                game_on = False
                score.game_over()
                print(f"Snake head at {snake.head.xcor()},{snake.head.ycor()}")
                print(f"collision with body at {seg.xcor()},{seg.ycor()}")
                break




#----------------------------

screen.exitonclick()