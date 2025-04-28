from turtle import Turtle

COLOR = "White"
START_COORDS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
MOVE_DISTANCE = 20
ANGLES = {"Right": 0,
          "Up": 90,
          "Left": 180,
          "Down": 270
          }

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake with 3 squares at the centre of the screen."""
        for point in START_COORDS:
            snake = Turtle("square")
            snake.color(COLOR)
            snake.penup()
            snake.teleport(point[0],point[1])
            self.segments.append(snake)

    def grow(self):
        """Increases the length of the snake by a single segment. Snake grows after colliding with food."""
        seg = Turtle("square")
        seg.color(COLOR)
        seg.penup()
        seg.teleport(self.segments[-1].xcor(),self.segments[-1].ycor())
        self.segments.append(seg)

    def move(self):
        """Moves the body of the snake to follow in the direction specified. Default direction is right. """
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_right(self):
        """The snake will turn right from its current position. This is the default facing position."""
        if self.head.heading() != ANGLES.get("Left"):
            self.head.setheading(ANGLES["Right"])

    def turn_left(self):
        """The snake will turn left from its current position."""
        if self.head.heading() != ANGLES.get("Right"):
            self.head.setheading(ANGLES["Left"])

    def up(self):
        """The snake will turn up from its current position."""
        if self.head.heading() != ANGLES.get("Down"):
            self.head.setheading(ANGLES["Up"])

    def down(self):
        """The snake will face down from its current position."""
        if self.head.heading() != ANGLES.get("Up"):
            self.head.setheading(ANGLES["Down"])

