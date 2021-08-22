# Basic Function for turtle
import turtle

def make_window(color, title):
    """ Create a window for turtle.
            color: Background color of the window
            title: Title of the window
            return: the window object    
    """
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, size):
    """ Create a new turtle.
            color: Color of the turtle
            size: Pen size
            return: the turtle object
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t

def print_square(turtle, size):
    """ Draw a square given a turtle and the length of the square.
            turtle: Turtle to move
            size: Length of the square
    """
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)