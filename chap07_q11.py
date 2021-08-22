# Solutions of Question 11, Chapter 7. 

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

# (angle, size)
data =  [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle, size) in data:
    t.left(angle)
    t.forward(size)

wd.mainloop()