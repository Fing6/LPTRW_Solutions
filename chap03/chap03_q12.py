# Question 12, Chapter 3
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("blue")
print(type(t))

l = 100
n = 12

t.shape("turtle")
t.penup()
for i in range(n):
  t.forward(l)
  t.stamp()
  t.forward(-20)
  t.pendown()
  t.forward(-10)
  t.penup()
  t.forward(-70)
  t.left(360 / n)

wn.mainloop()
