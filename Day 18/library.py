from random import randint, choice, uniform
import colorgram

shapes = [
    {"name": "triangle", "sides" : 3, "turn_angle" : 120},
    {"name": "square", "sides" : 4, "turn_angle" : 90},
    {"name": "pentagon", "sides" : 5, "turn_angle" : 72},
    {"name": "hexagon", "sides" : 6, "turn_angle" : 60},
    {"name": "heptagon", "sides" : 7, "turn_angle" : 51.43},
    {"name": "octagon", "sides" : 8, "turn_angle" : 45},
    {"name": "nonagon", "sides" : 9, "turn_angle" : 40},
    {"name": "decagon", "sides" : 10, "turn_angle" : 36},
]
colours = [
    "aquamarine3", "brown2", "burlywood", "black", "CadetBlue", "DarkGreen", "DarkOliveGreen3", "DarkViolet", "firebrick1", "LightSalmon1"
]
directions = [
        "right","left","straight"
    ]
def change_direction(t_name):
    """Set the turtle to turn to a random direction either left or right by a random number of degrees"""
    dir = choice(directions)
    if dir == directions[0]:
        return t_name.right(randint(10,61))
    elif dir == directions[1]:
        return t_name.left(randint(10, 61))
    else:
        pass

def random_color():
    """Returns a random RGB colour tuple in the form (r,g,b)."""
    r = uniform(0.0,1.0)
    g = uniform(0.0,1.0)
    b = uniform(0.0,1.0)
    color = (r,g,b)
    return color

def spirograph(t_name):
    """The turtle draws a spirograph with each drawn circle a random colour. 36 Circles are drawn in total."""
    new_pos = 0.00
    t_name.speed("fastest")
    for turn in range(0,36):
        t_name.pencolor(random_color())
        t_name.circle(100)
        new_pos += 10.0
        t_name.setheading(new_pos)

def draw_polygons(t_name):
    """The turtle draws a number of regular polygons from triangle (3 sides) to decagon (10 sides) imposed on each other, with each shape being a random colour."""
    for shape in shapes:
        t_name.pencolor(random_color())
        for i in range(0,shape["sides"]):
           t_name.forward(100)
           t_name.left(shape["turn_angle"])

def extract_colours():
    rgb_colours = []
    all_colours = colorgram.extract("image.jpg",30)
    for colour in all_colours:
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b
        rgb_colours.append((r,g,b))
        return rgb_colours

def paint_spots(t_name, num_spots,num_rows):
    """Draws a Damien Hirst-type spot painting with rows of random coloured spots of a given size. num_spots specifies the number of spots per row, and num_rows specifies the number of rows the painting should have."""
    y = -250
    for row in range(0,num_rows):
        x = -250
        y += 50
        t_name.penup()
        t_name.goto(x,y)
        for spot in range(0,num_spots):
            colour = random_color()
            t_name.pen(fillcolor = colour, pencolor = colour)
            t_name.pendown()
            t_name.begin_fill()
            t_name.circle(10)
            t_name.end_fill()
            t_name.penup()
            x += 50
            t_name.goto(x,y)