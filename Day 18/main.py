from turtle import Turtle, Screen
#from turtle import * - asterisk denotes all classes within the module - not good practice
#create aliases for imported modules with long/difficult names e.g. import turtle_sdf_sdf_34 as turt
from library import paint_spots

timmy = Turtle()
timmy.color("CadetBlue4")
timmy.speed("fastest")
timmy.hideturtle()
paint_spots(timmy,10,10)

my_screen = Screen()
my_screen.exitonclick()