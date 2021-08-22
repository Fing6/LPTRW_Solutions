# Question 3, Chapter 4
# Regular Polygon

import setup

# draw polygon
def draw_polygon(t, n, sz):
    for i in range(n):
        setup.print_square(t, sz)
        t.left(360 / n)

# main
wd = setup.make_window("lightgreen", "Regular Polygon")
tess = setup.make_turtle("blue", 2)

draw_polygon(tess, 20, 50)
# 8?

wd.mainloop()
    