# Question 1, Chapter 4
# Five Squares

import setup

# Main
wd = setup.make_window("lightgreen", "Five Squares")
t = setup.make_turtle("pink", 5)
n = 5
size = 20

for i in range(n):
    setup.print_square(t, size)
    t.penup()
    t.forward(2 * size)
    t.pendown()

wd.mainloop()


