# Solutions of Question 12, Chapter 7. 

""" Set up a list of pairs so that the turtle draws a house 
    with a cross through the centre.
    This should be done without going over any of the lines / edges more than once,
    and without lifting your pen."""

import turtle

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, size):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t

# Main
wd = make_window("white", "Advanved Drunk Pirate")
t = make_turtle("black", 2)

for i in range(4):
    t.forward(100)
    t.left(90)

t.left(45)
t.forward(100 * 2 ** 0.5)
for i in range(2):
    t.left(90)
    t.forward(50 * 2 ** 0.5)
t.left(90)
t.forward(100 * 2 ** 0.5) 

wd.mainloop()