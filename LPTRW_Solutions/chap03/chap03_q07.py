# Question 7, Chapter 3
import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.color("red")

l = 100
data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for d in data:
  t.left(d)
  t.forward(l)

wn.mainloop()
