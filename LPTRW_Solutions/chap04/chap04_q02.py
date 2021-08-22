# Question 2, Chapter 4
# Nested Squares

import setup

# Main
wd = setup.make_window("lightgreen", "Five Squares")
t = setup.make_turtle("deeppink", 4)
n = 5
size = 20

for i in range(n):
    setup.print_square(t, size)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
    size += 20

wd.mainloop()