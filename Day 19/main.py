from turtle import Turtle, Screen
from library import *

screen = Screen()
tim = Turtle()

def move_forwards():
    """The turtle will move forward by the specified pace. t-name specifies the turtle object"""
    tim.forward(10)

def move_backwards():
    """The turtle will move backwards by the specified pace. t-name specifies the turtle object"""
    #tim.left(180)
    #move_forwards()
    tim.backward(10)

def turn_right():
    """The turtle will turn clockwise from its current position. t-name specifies the turtle object"""
    tim.right(90)

def turn_left():
    """The turtle will turn anti-clockwise from its current position. t-name specifies the turtle object"""
    tim.left(90)

def clear_sketch():
    """Clears the entire board so a new sketch can be drawn. Turtle returns to its starting position."""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key = "w",fun = move_forwards)
screen.onkey(key = "s",fun = move_backwards)
screen.onkey(key = "a",fun = turn_left)
screen.onkey(key = "d",fun = turn_right)
screen.onkey(key = "c",fun = clear_sketch)

screen.exitonclick()