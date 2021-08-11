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

# draw polygon
def draw_polygon(t, n, sz):
    for i in range(n):
        print_square(t, sz)
        t.left(360 / n)

# main
wd = make_window("lightgreen", "Regular Polygon")
tess = make_turtle("blue", 2)

draw_polygon(tess, 20, 50)
# 8?

wd.mainloop()
    