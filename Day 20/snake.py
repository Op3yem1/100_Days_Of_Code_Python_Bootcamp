from turtle import Screen, Turtle
import time

START_COORDS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
MOVE_DISTANCE = 20
ANGLES = {"Up": 90,
          "Down": 270,
          "Right": 0,
          "Left": 180}

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake with 3 squares at the centre of the screen."""
        for point in START_COORDS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.teleport(point[0],point[1])
            self.segments.append(snake)

    def head_move(self):
        """Moves the head of the snake by a single step."""


    def move(self):
        """Moves the body of the snake to follow in the direction of the head. """
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_right(self):
        """The snake will face West from its current position. This is the default facing position."""
        if self.head.heading() != ANGLES.get("Left"):
            self.head.setheading(0)

    def turn_left(self):
        """The snake will face East from its current position."""
        if self.head.heading() != ANGLES.get("Right"):
            self.head.setheading(180)

    def up(self):
        """The snake will face North from its current position."""
        if self.head.heading() != ANGLES.get("Down"):
            self.head.setheading(90)

    def down(self):
        """The snake will face South from its current position."""
        if self.head.heading() != ANGLES.get("Up"):
            self.head.setheading(270)

   # def hit_wall(self):
        #if self.segments[0].xcor() >= screen.setworldcoordinates[0]:
         #   return True
       # return False