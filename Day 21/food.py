from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        #self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.4,stretch_wid=0.4)
        self.color("CadetBlue1")
        self.appear()

    def appear(self):
        point = {"x": random.uniform(-280.0,280.0), "y": random.uniform(-280.0,280.0)}
        self.speed("fastest")
        self.teleport(point["x"], point["y"])

