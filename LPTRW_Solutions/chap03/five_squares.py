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

def print_square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

# Main
wd = make_window("lightgreen", "Five Squares")
t = make_turtle("pink", 5)
n = 5
size = 20

for i in range(n):
    print_square(t, size)
    t.penup()
    t.forward(2 * size)
    t.pendown()

wd.mainloop()


